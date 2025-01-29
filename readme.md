# Blog Writing AI

This repository contains a Streamlit application that uses AI agents to generate professional, SEO-optimized blog posts based on user inputs. The application leverages the `crewai` library and the `SerperDevTool` for extracting relevant information and generating content.

## 🚀 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rugedp/blog-writing-ai.git
    cd blog-writing-ai
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your API keys in the Streamlit secrets file:
    ```plaintext
    [secrets]
    SERPER_API_KEY = "your_serper_api_key"
    SAMBANOVA_API_KEY = "your_sambanova_api_key"
    ```

## 🛠️ Usage

1. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Fill in the required fields:
    - **Company Name**: Enter the name of the company.
    - **Topic**: Enter the topic for the blog post.
    - **Tone**: Enter the desired tone (e.g., professional, friendly).
    - **Social Media**: Enter the social media platform (e.g., LinkedIn, Twitter).

4. Click the "Generate Blog" button to generate the blog post.

5. The generated blog post will be displayed on the page, and you can download it as a markdown file.

## 📂 Code Overview

- `main.py`: The main Streamlit application file.
- `crewai`: Library used for creating AI agents and tasks.
- `SerperDevTool`: Tool used for extracting information from Google Search API.

### 🤖 Agents

- **Research Agent**: Extracts detailed, accurate, and relevant information about a company's topic from credible sources.
- **Blog Writer Agent**: Writes engaging, SEO-optimized blog posts that reflect the company's voice and industry insights.

### 📝 Tasks

- **Research Task**: Gathers comprehensive and up-to-date information about the given company and topic.
- **Blog Task**: Writes a well-structured, engaging, and SEO-optimized blog post based on extracted research data.

### 👥 Crew

The `Crew` class coordinates the agents and tasks in a sequential process to generate the final blog post.

## 🔧 Customization

You can customize the agents, tasks, and process by modifying the `main.py` file. Adjust the LLM models, roles, goals, and backstories to fit your specific needs.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📧 Contact

For any questions or inquiries, please contact [Rugved Patil](mailto:rugvedp00@gmail.com).

## 🌟 Benefits for Companies

Using the Blog Writing AI application can significantly benefit companies in several ways:

1. **⏱️ Time Efficiency**: Automates the blog writing process, saving valuable time for marketing teams.
2. **🔄 Consistency**: Ensures consistent quality and tone across all blog posts, aligning with the company's brand voice.
3. **📈 SEO Optimization**: Generates SEO-friendly content that can improve search engine rankings and drive more organic traffic.
4. **💰 Cost-Effective**: Reduces the need for hiring external content writers, lowering overall content creation costs.
5. **📊 Scalability**: Easily scales content production to meet the demands of various marketing campaigns and initiatives.

## 🌐 Real-World Applications

The Blog Writing AI application can be utilized in various real-world scenarios, including:

1. **📣 Content Marketing**: Helps marketing teams produce high-quality blog posts that engage audiences and promote products or services.
2. **📱 Social Media Management**: Generates tailored content for different social media platforms, enhancing online presence and audience interaction.
3. **🏢 Corporate Communications**: Assists in creating informative and professional blog posts for internal and external communications.
4. **📊 Industry Analysis**: Provides detailed research and insights on industry trends, helping companies stay informed and competitive.
5. **🧠 Thought Leadership**: Enables companies to publish authoritative and insightful articles, establishing themselves as thought leaders in their industry.