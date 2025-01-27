# LeadGen Project

## Setup Instructions

1. **Create a Data Folder**
    - Please create a `data` folder in the root directory of the project. This folder will be used to store output files and is ignored in the git repository.

2. **Create a Keys Environment File**
    - You need to create a `keys.env` file in the root directory of the project to store the API keys for the LLM clients.
    - The `keys.env` file should have the following format:
      ```
      OPENA_API_KEY=your_opena_api_key_here
      GEMINI_API_KEY=your_gemini_api_key_here
      ```

Make sure to replace `your_opena_api_key_here` and `your_gemini_api_key_here` with your actual API keys.