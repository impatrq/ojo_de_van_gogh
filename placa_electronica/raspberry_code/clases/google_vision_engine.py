class GoogleVisionEngine:
    """
    Clase para guardar la imagen y el cliente
    """

    def __init__(self, image_path, client):
        self.image_path = image_path
        self.client = client
