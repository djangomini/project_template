from djangomini.controllers import Controller


class MainController(Controller):
    """Render home page and some other 'root' urls."""

    def get(self):
        """Render homepage."""
        return self.html('Main page')
