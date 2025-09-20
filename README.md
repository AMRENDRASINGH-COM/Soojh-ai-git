
## 📁 Project Structure

```
📦 Soojh-AI/
├── 🤖 chatbot.py          # Interactive chat interface
├── 📊 graph.py            # LangGraph workflow definition  
├── 🎯 node.py             # Graph nodes and state management
├── 🛠️ tools.py            # External research tools
├── 🧠 llm.py              # LLM configurations and models
├── ⚙️ agent.py            # Google ADK agent setup
├── 📄 README.md           # This file
├── 🔐 .env.example        # Environment variable template
├── 📋 requirements.txt    # Python dependencies
└── 🚫 .gitignore          # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- OpenAI API key
- Git

### Installation

1. **Clone the repository**
   ```
   git clone https://github.com/AMRENDRASINGH-COM/Soojh-ai-git.git
   cd Soojh-ai-git
   ```

2. **Create virtual environment**
   ```
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```
   cp .env.example .env
   # Edit .env file and add your OpenAI API key:
   # OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**
   ```
   # Interactive chatbot
   python chatbot.py
   
   # Or import as module
   from graph import build_graph
   graph = build_graph()
   ```

## 💻 Usage Examples

### Basic Chat Interaction
```
from chatbot import chat_with_bot

# Simple conversation
response = chat_with_bot("What is machine learning?")
print(response)

# Research query
response = chat_with_bot("Find recent papers on transformer architecture")
print(response)
```

### Advanced Graph Usage
```
from graph import build_graph

# Build the LangGraph workflow
graph = build_graph()

# Stream responses for complex queries
events = graph.stream({
    "messages": [("user", "Explain quantum computing with recent research")]
}, stream_mode="values")

for event in events:
    print(event["messages"][-1].content)
```

### Multi-Agent System
```
from agent import root_agent
from google.adk.apps import AdkApp

# Create ADK application
app = AdkApp(agent=root_agent, enable_tracing=True)

# Start interactive session
session = app.create_session(user_id="user123")

# Query the multi-agent system
for event in app.stream_query(
    user_id="user123",
    session_id=session.id,
    message="Research the latest developments in AI safety"
):
    print(event)
```

## 🛠️ Core Components

### 🎯 Graph Nodes (`node.py`)
- **State Management**: TypedDict-based state handling
- **LLM Integration**: GPT-4o with tool binding
- **Message Processing**: Conversation flow management

### 📊 Workflow Graph (`graph.py`)
- **StateGraph**: LangGraph-based workflow orchestration
- **Tool Integration**: Conditional tool usage based on queries
- **Flow Control**: START → Chatbot → Tools → END

### 🛠️ Research Tools (`tools.py`)
- **Wikipedia Integration**: Real-time knowledge retrieval
- **Arxiv Access**: Academic paper search and analysis
- **Configurable Limits**: Response length and result count control

### 🤖 Multi-Agent System (`agent.py`)
- **Google ADK Integration**: Enterprise agent framework
- **Sub-Agent Coordination**: Specialized agent delegation
- **LangGraph Bridge**: Seamless integration between systems

## 🎯 Use Cases

### 🔬 Research Assistant
- Academic paper analysis and summarization
- Cross-reference verification with Wikipedia
- Literature review automation
- Citation and reference management

### 💬 Intelligent Chatbot
- Context-aware conversations
- Multi-turn dialogue handling
- Domain-specific knowledge queries
- Real-time information retrieval

### 🏢 Enterprise Applications
- Customer support automation
- Internal knowledge base queries
- Research and development assistance
- Decision support systems

## 🔧 Configuration

### Environment Variables
```
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=soojh-ai
```

### Model Configuration
```
# In llm.py
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o",           # Or gpt-4, gpt-3.5-turbo
    temperature=0.1,          # Adjust creativity
    max_tokens=2000          # Response length limit
)
```

## 📚 Dependencies

### Core Libraries
- **langchain-openai**: OpenAI integration
- **langchain-community**: Community tools and utilities  
- **langgraph**: Graph-based workflow orchestration
- **google-adk**: Google Agent Development Kit
- **python-dotenv**: Environment variable management

### Research Tools
- **wikipedia**: Wikipedia API wrapper
- **arxiv**: Academic paper access
- **pydantic**: Data validation and settings

## 🚀 Advanced Features

### Custom Agent Creation
```
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Create specialized agent
research_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    name="research_specialist",
    description="Expert in academic research and analysis",
    instruction="Provide detailed, well-sourced research responses",
    tools=[wikipedia_tool, arxiv_tool]
)
```

### Custom Tool Integration
```
from langchain.tools import BaseTool

class CustomTool(BaseTool):
    name = "custom_research_tool"
    description = "Specialized tool for domain-specific research"
    
    def _run(self, query: str) -> str:
        # Your custom tool implementation
        return f"Custom research result for: {query}"

# Add to tools list
tools.append(CustomTool())
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup
```
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Code formatting
black .
isort .

# Type checking
mypy .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain Team**: For the excellent LangGraph framework
- **Google Cloud**: For the Agent Development Kit
- **OpenAI**: For the powerful GPT models
- **Arxiv & Wikipedia**: For open access to knowledge

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/AMRENDRASINGH-COM/Soojh-ai-git/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AMRENDRASINGH-COM/Soojh-ai-git/discussions)
- **Documentation**: [Project Wiki](https://github.com/AMRENDRASINGH-COM/Soojh-ai-git/wiki)

---

**Made with ❤️ by [Amrendra Singh](https://github.com/AMRENDRASINGH-COM)**

*Soojh AI - Where Intelligence Meets Innovation* 🚀
"@ > README.md
```

This comprehensive README includes:
- Professional branding with badges
- Clear architecture diagram  
- Complete installation guide
- Usage examples for all components
- Detailed project structure
- Advanced configuration options
- Contributing guidelines
- Professional formatting

Copy and paste this command to create your README.md file![1][2][3][4][5]
