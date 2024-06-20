from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def read_rootLeague(self):
        self.client.get("/league")
    @task
    def read_rootlistTeam(self):
        self.client.get("/league/4")
    @task
    def read_rootTeams(self):
        self.client.get("/Teams/82")
    @task
    def read_rootJoueur(self):
        self.client.get("/Joueur/4060197324")