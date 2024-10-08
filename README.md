# CodePipelineX
This project is demonstrate how to create a code based on the user questions and test in the pipeline.

**prerequisites**
* Python 3.10+

**References**
* [Managing environments for deployment](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)
* [How to access environment secrets from a Github workflow?](https://stackoverflow.com/questions/66521958/how-to-access-environment-secrets-from-a-github-workflow)

**Project Docs**
* [Main Documentation](https://docs.google.com/document/d/1Ozry-lw7SFePsViqE2vgJOP6yUgEQbezWWRHMZhIP9E/edit?usp=sharing)

# .env
Create a .env file in your root directory and paste this code. please don't forget to replace your api key.
```py
OPENAI_API_KEY=<YOUR_API_KEY>
```

# Local setup
### Step 1:
clone the project using this command
```
git clone https://github.com/Antony-M1/CodePipelineX.git
```

### Step 2:
Get into the project folder and create a environment and activate the environment.
For linux ubuntu
```
python -m venv venv
```
```
source venv/bin/activate
```

### Step 3:
Install all the dependencies
```
pip install -r requirements.txt
```

### Step 4:
Run the following command. before running this command make sure you created all the `.env` file with neccessary credentials.
```
python codex_code_generator.py > generated_code.py
```
