import geojson
import parse as p

def create_map(data_file):
    """Creates a GeoJSON file.

    Returns a GeoJSON file that can be rendered in a GitHub
    Gist at gist.github.com. Just copy the output file and
    paste into a new Gist, then create either a public or
    private gist. GitHub will automatically render the GeoJSON 
    file as a map.
    """

