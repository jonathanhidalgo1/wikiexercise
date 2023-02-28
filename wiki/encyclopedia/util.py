import re
import markdown2


from django.core.files.base import ContentFile
from django.core.files.storage import default_storage



def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
    
def convert_entry(title):
    if default_storage.exists(f"entries/{title}.html"):
        default_storage.delete(f"entries/{title}.html")
        f = default_storage.open(f"entries/{title}.md")
        html = markdown2.markdown(f.read().decode("utf-8"))
        save_html = default_storage.save(f"entries/{title}.html", ContentFile(html))
        return save_html
        
    else:
        f = default_storage.open(f"entries/{title}.md")
        html = markdown2.markdown(f.read().decode("utf-8"))
        save_html = default_storage.save(f"entries/{title}.html", ContentFile(html))
        return save_html
        
def get_entry_html(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.html")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
