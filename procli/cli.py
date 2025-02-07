import os
import subprocess
import sys
import click

def run_command(command, cwd=None):
    """Helper to run a command via subprocess and handle errors."""
    try:
        subprocess.run(command, cwd=cwd, check=True)
    except subprocess.CalledProcessError as err:
        click.echo(f"Error: {err}")
        sys.exit(1)

@click.group()
def cli():
    """
    procli - A CLI tool for creating Python projects using Pipenv.
    
    This tool wraps Pipenv commands to:
      - Initialize a new project with a virtual environment.
      - Manage dependencies easily (add, remove, update).
    """
    pass

@cli.command()
@click.argument('project_name')
@click.option('--python', default='python3', help="Python version to use (e.g., python3.9)")
def init(project_name, python):
    """
    Initialize a new Python project with Pipenv.
    
    PROJECT_NAME: The name of the new project.
    """
    # Create the project directory if it doesn't exist.
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        click.echo(f"Created project directory: {project_name}")
    else:
        click.echo(f"Directory '{project_name}' already exists.")
    
    # Change directory into the project folder.
    os.chdir(project_name)
    
    # Initialize Pipenv with the specified Python version.
    click.echo(f"Initializing Pipenv with {python}...")
    run_command(["pipenv", "--python", python, "install"])
    
    # Create a sample main.py file if it does not exist.
    main_file = "main.py"
    if not os.path.exists(main_file):
        with open(main_file, "w") as f:
            f.write("def main():\n")
            f.write("    print('Hello from your new project!')\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    main()\n")
        click.echo(f"Created starter file: {main_file}")
    else:
        click.echo(f"Starter file '{main_file}' already exists.")
    
    click.echo("Project initialization complete!")
    click.echo("To activate the virtual environment, run 'pipenv shell' or execute your project with 'pipenv run python main.py'.")

@cli.command()
@click.argument('package')
def add(package):
    """
    Add a dependency to your project using Pipenv.
    
    PACKAGE: The package name (and optionally version, e.g., requests==2.28.0)
    """
    click.echo(f"Adding dependency: {package} ...")
    run_command(["pipenv", "install", package])
    click.echo("Dependency added.")

@cli.command()
@click.argument('package')
def remove(package):
    """
    Remove a dependency from your project using Pipenv.
    
    PACKAGE: The package name to remove.
    """
    click.echo(f"Removing dependency: {package} ...")
    run_command(["pipenv", "uninstall", package])
    click.echo("Dependency removed.")

@cli.command()
def install():
    """
    Install all dependencies from Pipfile.lock.
    
    Useful after cloning a project.
    """
    click.echo("Installing project dependencies...")
    run_command(["pipenv", "install"])
    click.echo("Dependencies installed.")

if __name__ == '__main__':
    cli()
