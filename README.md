# Knowledge Base Assistant

## Overview

Knowledge Base Assistant is a Python project that allows users to ask questions and receive answers from locally stored text documents.

The assistant searches through a collection of knowledge files and retrieves the most relevant information based on the user's query.

This project demonstrates fundamental concepts behind search engines, document retrieval systems, and AI knowledge assistants.

---

## Features

* Ask questions using natural language
* Search across multiple knowledge documents
* Retrieve relevant answers automatically
* Local document-based knowledge storage
* No internet connection required
* Easy to expand by adding new text files

---

## Project Structure

```text
Knowledge Base Assistant/

├── search_engine.py

└── documents/

    ├── python.txt
    ├── robotics.txt
    ├── arduino.txt
    ├── machine_learning.txt
    ├── ai.txt
    ├── computer.txt
    └── electronics.txt
```

---

## How It Works

1. Load all text files from the documents folder.
2. Store the contents as a local knowledge base.
3. Accept a question from the user.
4. Search for relevant topics and keywords.
5. Return the most relevant answer.

Example:

Question:

What is Python?

Answer:

Python is a programming language.

Python is used for machine learning, automation, web development and robotics.

---

## Example Usage

```text
Ask: what is python
```

Output:

```text
Python is a programming language.

Python is used for machine learning, automation, web development and robotics.

Python is beginner friendly and easy to learn.
```

---

## Technologies Used

* Python
* Pathlib
* File Handling
* Dictionaries
* Text Processing

---

## Concepts Learned

* File Handling
* Text Processing
* Information Retrieval
* Keyword Matching
* Knowledge Base Design
* Search Algorithms
* Python Data Structures

---

## Future Improvements

* TF-IDF Search Ranking
* Natural Language Processing (NLP)
* Fuzzy Matching
* Voice Input
* Graphical User Interface (Tkinter)
* Machine Learning-Based Retrieval
* Integration with Local LLMs
* PDF Knowledge Sources

---

## Real-World Applications

* Local AI Assistants
* Offline Knowledge Systems
* Internal Company Documentation Search
* Educational Learning Assistants
* FAQ Retrieval Systems
* Document Search Tools

---

## Sample Knowledge Topics

* Python
* Robotics
* Arduino
* Machine Learning
* Artificial Intelligence
* Computers
* Electronics

New topics can be added by simply creating additional text files inside the documents folder.

---

## Conclusion

This project demonstrates how a simple document retrieval system can be built using Python. It serves as a foundation for more advanced AI assistants, search engines, and knowledge retrieval systems by allowing users to interact with locally stored information through natural language questions.
