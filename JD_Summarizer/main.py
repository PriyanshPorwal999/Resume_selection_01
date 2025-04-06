import argparse
import json
from ollama_client import OllamaClient
from batch_processor import process_csv_file

def main():
    parser = argparse.ArgumentParser(description='Process job descriptions from a CSV file')
    parser.add_argument('csv_file', help='Path to the CSV file containing job descriptions')
    parser.add_argument('--output', default='job_summaries.json', help='Output JSON file path (default: job_summaries.json)')
    parser.add_argument('--model', default='mistral', help='Ollama model to use (default: mistral)')
    
    args = parser.parse_args()
    
    ollama_client = OllamaClient(model_name=args.model)
    
    try:
        test_response = ollama_client.generate("Hi")
        print(f"Ollama is available with model: {args.model}")
    except Exception as e:
        print(f"Warning: Ollama is not available or model '{args.model}' is not loaded. Error: {str(e)}")
        print("Continue with fallback methods...")
        ollama_client = None
    
    results = process_csv_file(args.csv_file, ollama_client)
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"Processed {len(results)} job descriptions. Results saved to {args.output}")

if __name__ == "__main__":
    main()