#!/bin/bash
#SBATCH --job-name=kaggle-dl
#SBATCH --output=logs/install_dataset_%j.out
#SBATCH --error=logs/install_dataset_%j.err
#SBATCH --time=1-00:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G

# Email settings
#SBATCH --mail-type=END,FAIL                # Send email on job completion or failure
#SBATCH --mail-user=your.email@example.com  # Replace with your email

# Always run from the directory the job was submitted in
cd "$SLURM_SUBMIT_DIR"

# Activate the virtual environment
source venv/bin/activate

# Create logs folder if it doesn't exist
mkdir -p logs

# Run your dataset download script
python src/install.py
