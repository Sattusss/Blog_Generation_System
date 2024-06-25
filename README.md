# Blog Generator Project

This project uses Streamlit and LangChain to generate blog posts based on user inputs. The LangChain library leverages the LLama 2 model for generating content, making it easy to create tailored blog posts for different audiences.

## Installation

1. **Clone the repository:**
    ```sh
    git clone [https://github.com/Sattusss/Blog_Generation_System]
    cd [Blog_Generation_System]
    ```

2. **Install required packages:**
    ```sh
    pip install streamlit langchain ctransformers
    ```

3. **Download the LLama 2 model:**
    Ensure the model file `llama-2-7b-chat.ggmlv3.q8_0.bin` is placed in the `models` directory.

## Usage

Run the Streamlit app:
```sh
streamlit run app.py
```

## Project Structure

- `app.py`: The main application file containing the Streamlit interface and the blog generation logic.
- `models`: Directory to store the LLama 2 model file.

## Explanation

- **Function `getLLamaresponse`**: Initializes the LLama model and creates a prompt template for generating the blog post. It then formats the prompt with the user's input and retrieves the response from the model.
- **Streamlit interface**: The app takes user inputs for the blog topic, number of words, and the target audience, and displays the generated blog post upon submission.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to contribute to this project by opening issues and submitting pull requests. For any questions, please contact [your_email@example.com].
