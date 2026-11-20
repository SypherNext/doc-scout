# setup_project.sh: Creates a new AI project with venv and core deps
PROJECT_NAME=${1:-ai_project}

echo "Creating project: $PROJECT_NAME"
mkdir "$PROJECT_NAME"
cd "$PROJECT_NAME"

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing core AI packages..."
pip install numpy pandas requests openai scikit-learn

echo "Freezing dependencies..."
pip freeze > requirements.txt

echo "Project ready! Activate with: cd $PROJECT_NAME && source venv/bin/activate"
