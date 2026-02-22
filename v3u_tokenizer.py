import tiktoken
import sys

def get_tokens(text, model="o200k_base"):
    try:
        encoding = tiktoken.get_encoding(model)
    except ValueError:
        encoding = tiktoken.encoding_for_model("gpt-4o")
    
    tokens = encoding.encode(text)
    return tokens

def analyze_text(text, name="Text"):
    tokens = get_tokens(text)
    num_tokens = len(tokens)
    num_chars = len(text)
    ratio = num_chars / num_tokens if num_tokens > 0 else 0
    
    print(f"--- {name} ---")
    print(f"Content: {text}")
    print(f"Tokens: {num_tokens}")
    print(f"Characters: {num_chars}")
    print(f"Chars/Token: {ratio:.2f}")
    print("-" * (len(name) + 8))
    return num_tokens

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_text(" ".join(sys.argv[1:]))
    else:
        # Example usage for comparison if run without args
        ex1_en = "Incident reported at 09:14. API leak detected. Latency increased from 5s to 15s. Human intervention required. Status: Active."
        ex1_p2 = ".I L.A 123 0914 V.L 5s->15s /h V.A"
        ex1_p3 = "L.A 123 0914 V.L 5s->15s /h V.A"

        ex2_en = "Task A is critical priority, assigned 8 points. Description: fix memory leak. Assigned to #MN. Due in 2 days."
        ex2_p2 = ".T A crit 8 f-leak #MN - 2d"
        ex2_p3 = "A crit 8 f-leak #MN - 2d"

        ex3_en = "I confirm that I have received the message and everything is stable."
        ex3_p2 = ".S K.S #XX"
        ex3_p3 = "K.S #XX"

        print("P3 EFFICIENCY COMPARISON (o200k_base)\n")
        
        t1_en = analyze_text(ex1_en, "Ex 1: English")
        t1_p2 = analyze_text(ex1_p2, "Ex 1: P2")
        t1_p3 = analyze_text(ex1_p3, "Ex 1: P3")
        print(f"Ex 1 Savings: P2={t1_en/t1_p2:.1f}x, P3={t1_en/t1_p3:.1f}x\n")

        t2_en = analyze_text(ex2_en, "Ex 2: English")
        t2_p2 = analyze_text(ex2_p2, "Ex 2: P2")
        t2_p3 = analyze_text(ex2_p3, "Ex 2: P3")
        print(f"Ex 2 Savings: P2={t2_en/t2_p2:.1f}x, P3={t2_en/t2_p3:.1f}x\n")

        t3_en = analyze_text(ex3_en, "Ex 3: English")
        t3_p2 = analyze_text(ex3_p2, "Ex 3: P2")
        t3_p3 = analyze_text(ex3_p3, "Ex 3: P3")
        print(f"Ex 3 Savings: P2={t3_en/t3_p2:.1f}x, P3={t3_en/t3_p3:.1f}x\n")
