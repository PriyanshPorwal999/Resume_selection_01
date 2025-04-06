import ollama
import smtplib
from email.mime.text import MIMEText
import os
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_email_content(name, position, is_shortlisted):
    """
    Generates email content using the locally hosted Ollama model.

    Args:
        name (str): Applicant's name.
        position (str): Job position.
        is_shortlisted (bool): True if shortlisted, False otherwise.

    Returns:
        str: The generated email body.
    """
    if is_shortlisted:
        prompt = (
            f"Write a professional email to {name} congratulating them on being shortlisted for the {position} role at Accenture and your name is 'Recruiting Team, Accenture'. "
            "Start with Congratulations!... "
            "Mention that their application stood out due to their skills and experience. "
            "Inform them that the hiring team will contact them within a week to schedule an interview."
            "You don't need to tell me if you have generated the email or not. "
            "Don't need to write the subject line. "
            "Just write the email body."
        )
    else:
        prompt = (
            f"Compose a polite and professional email to {name} thanking them for applying to the {position} role at Accenture and your name is 'Recruiting Team, Accenture'. "
            "Inform them that they were not shortlisted after careful consideration. "
            "Encourage them to apply for future opportunities."
            "You don't need to tell me if you have generated the email or not. "
            "Don't need to write the subject line. "
            "Just write the email body."
        )
    
    # Use the locally hosted Ollama model to generate the email content
    try:
        response = ollama.generate(model="llama3.2:1b", prompt=prompt)
        logger.info("Successfully generated email content with Ollama.")
        return response['response']
    except Exception as e:
        logger.error(f"Error generating email content with Ollama: {e}")
        raise

def send_email(to_email, subject, body, use_ssl=False):
    """
    Sends an email using Gmail's SMTP server.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body.
        use_ssl (bool): If True, use SSL (port 465); if False, use TLS (port 587).

    Environment Variables:
        SENDER_EMAIL: Your Gmail address.
        SENDER_PASSWORD: Your Gmail App Password.

    Raises:
        ValueError: If credentials are missing.
        Exception: If email sending fails.
    """
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    
    if not sender_email or not sender_password:
        logger.error("SENDER_EMAIL or SENDER_PASSWORD environment variables are not set.")
        raise ValueError("Please set SENDER_EMAIL and SENDER_PASSWORD environment variables.")
    
    # Create the email message
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    try:
        if use_ssl:
            logger.info("Attempting to connect to smtp.gmail.com:465 (SSL)...")
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=60) as server:
                logger.info("Connected to SMTP server with SSL.")
                server.login(sender_email, sender_password)
                logger.info("Logged in successfully.")
                server.sendmail(sender_email, to_email, msg.as_string())
                logger.info(f"Email sent successfully to {to_email} via SSL.")
        else:
            logger.info("Attempting to connect to smtp.gmail.com:587 (TLS)...")
            with smtplib.SMTP('smtp.gmail.com', 587, timeout=60) as server:
                logger.info("Connected to SMTP server.")
                server.starttls()
                logger.info("TLS started.")
                server.login(sender_email, sender_password)
                logger.info("Logged in successfully.")
                server.sendmail(sender_email, to_email, msg.as_string())
                logger.info(f"Email sent successfully to {to_email} via TLS.")
    except Exception as e:
        logger.error(f"Error sending email to {to_email}: {e}")
        raise

def main():
    """
    Main function to generate email content with Ollama and send it.
    """
    # Example applicant data (modify as needed)
    name = "Jane Smith"
    position = "Data Analyst"
    is_shortlisted = True
    to_email = "jane.smith@example.com"
    subject = "Update on Your Application for Data Analyst"
    
    # Generate email content using Ollama
    try:
        email_body = generate_email_content(name, position, is_shortlisted)
        logger.info(f"Generated email content:\n{email_body}")
    except Exception as e:
        logger.error(f"Failed to generate email content: {e}")
        return
    
    # Send the email, trying TLS first and falling back to SSL if needed
    try:
        send_email(to_email, subject, email_body, use_ssl=False)
    except Exception as e:
        logger.warning("TLS connection failed, retrying with SSL...")
        try:
            send_email(to_email, subject, email_body, use_ssl=True)
        except Exception as e:
            logger.error("SSL connection also failed. Unable to send email.")

if __name__ == "__main__":
    if not os.getenv('SENDER_EMAIL') or not os.getenv('SENDER_PASSWORD'):
        logger.error("Error: Set SENDER_EMAIL and SENDER_PASSWORD environment variables first.")
    else:
        main()