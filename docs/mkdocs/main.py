import os

def define_env(env):
    """
    This function is called by mkdocs-macros-plugin to define custom macros.
    """
    @env.macro
    def include_file(filename):
        """
        Reads a Markdown file and returns its content as a string.
        """
        docs_dir = env.conf['docs_dir']  # Correct way to get docs_dir
        project_dir = env.project_dir    # Still valid
        filepath = os.path.join(project_dir, docs_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"**Error: file '{filename}' not found.**"
