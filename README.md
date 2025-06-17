# Marketing Agency


## Overview

This AI-powered assistant is engineered to enhance the capabilities of creative agencies when launching new websites or products. The process commences with an intelligent agent that guides users in selecting a creative product name , ensuring it aligns perfectly with the website's subject matter or the product's identity. 
## Agent Details

The key features of the Marketing Agency include:

| Feature | Description |
| --- | --- |
| **Interaction Type** | Conversational |
| **Complexity**  | Medium |
| **Agent Type**  | Multi Agent |
| **Components**  | Tools: built-in Google Search |
| **Vertical**  | Marketing |


## Setup and Installation

1.  **Prerequisites**

    *   Python 3.11+
    * A project on Google Cloud Platform
    * Google Cloud CLI
        *   For installation, please follow the instruction on the official
            [Google Cloud website](https://cloud.google.com/sdk/docs/install).

2.  **Installation**

    ```bash
    # Clone this repository.
    git clone https://github.com/adhish-endava/endava-apac-agentthon.git
    cd endava-apac-agentthon/marketing-agency
    # Install the package and dependencies.
    pip install -r requirements.txt
    ```

3.  **Configuration**

    *   Set up Google Cloud credentials.

        *   You may set the following environment variables in your shell, or in
            a `.env` file instead.

        ```bash
        export GOOGLE_GENAI_USE_VERTEXAI=true
        export GOOGLE_CLOUD_PROJECT=<your-project-id>
        export GOOGLE_CLOUD_LOCATION=us-central1
        export GOOGLE_CLOUD_STORAGE_BUCKET=<your-storage-bucket>  # Only required for deployment on Agent Engine
        ```

    *   Authenticate your GCloud account.

        ```bash
        gcloud auth application-default login
        gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT
        ```

## Running the Agent

**Using `adk`**

ADK provides convenient ways to bring up agents locally and interact with them.
You may talk to the agent using the CLI:

```bash
export PATH=$PATH:$HOME/.local/bin #Add ADK to your PATH
adk run marketing_agency
```

Or on a web interface:

```bash
 adk web
```

If you are running in it Google Cloud Shell you can use the 'web preview' sescion on port 8000 to test your application UI