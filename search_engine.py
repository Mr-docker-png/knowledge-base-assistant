from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "documents"

# Load knowledge
knowledge = {}

for file_path in DOCS_DIR.glob("*.txt"):

    topic = file_path.stem.lower()

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    knowledge[topic] = content

print("Knowledge Base Assistant")
print("Type 'exit' to quit")

while True:

    question = input("\nAsk: ").lower()

    if question == "exit":
        break

    found = False

    for topic, answer in knowledge.items():

        if topic in question:

            print("\nAnswer:\n")
            print(answer)

            found = True
            break

    if not found:

        # Smart fallback search
        best_match = None
        best_score = 0

        for topic, answer in knowledge.items():

            score = 0

            words = question.split()

            for word in words:

                if word in answer.lower():
                    score += 1

            if score > best_score:
                best_score = score
                best_match = answer

        if best_score > 0:

            print("\nClosest Answer:\n")
            print(best_match)

        else:

            print("\nSorry, I don't know the answer.")