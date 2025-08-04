import uuid
import time
import random
from datetime import datetime, timedelta
from utils.social_media_api import SocialMediaAPI

class SocialMediaAgent:
    def __init__(self, params=None):
        self.agent_id = f"social-{str(uuid.uuid4())[:8]}"
        self.params = params or {}
        self.api = SocialMediaAPI()
        self.scheduled_posts = []
        print(f"Social Media Agent {self.agent_id} initialized")
    
    def schedule_post(self, platform, content, schedule_time=None):
        if not schedule_time:
            schedule_time = datetime.now() + timedelta(minutes=5)
        
        post = {
            "id": str(uuid.uuid4())[:8],
            "platform": platform,
            "content": content,
            "schedule_time": schedule_time.isoformat(),
            "status": "scheduled",
            "created_at": datetime.now().isoformat()
        }
        self.scheduled_posts.append(post)
        
        # Simulate scheduling
        print(f"Scheduled post for {platform} at {schedule_time}")
        return post
    
    def post_to_all_platforms(self, content):
        platforms = ["facebook", "twitter", "instagram", "linkedin", "tiktok"]
        results = []
        for platform in platforms:
            results.append(self.schedule_post(platform, content))
        return results
    
    def execute(self, task, params):
        if task == "schedule_post":
            return self.schedule_post(
                params.get("platform"),
                params.get("content"),
                params.get("schedule_time")
            )
        elif task == "post_to_all":
            return self.post_to_all_platforms(params.get("content"))
        else:
            raise ValueError(f"Unknown task: {task}")
    
    def generate_content(self, topic):
        """AI-generated social media content"""
        # Simulate content generation
        time.sleep(0.7)
        content = f"Check out our latest update on {topic}! #AI #Innovation"
        return {"content": content, "hashtags": ["#AI", "#Innovation", "#Tech"]}
