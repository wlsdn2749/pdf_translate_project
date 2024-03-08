from locust import HttpUser, task, between

TARGET_USER_COUNT = 300

class LocustTest(HttpUser):
    wait_time = between(1,2)
    
    @task
    def small_text(self): # Small Size Text Translations
        self.client.post("/translate", json={"text": "Six Factory System Tricks for Extensibility and Library Reuse"})
        
    @task
    def large_text(self): # Large Size Text Translations
        self.client.post("/translate", json={"text": "These days, many games employ a data-driven AI. \
                                                      In other words, the decision-making logic for the AI is not hardcoded in C++ but instead is placed in a configuration file \
                                                      (generally using XML or some similar format) and loaded at runtime. \
                                                      This file gener-ally  specifies the configuration of a variety of different types of polymorphic objects."})
        