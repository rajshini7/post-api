import random

def create_post_payload():
    return {
        "title": f"New Post {random.randint(1, 9999)}",
        "body": "This is a sample post body",
        "userId": 1
    }

def put_post_payload(post_id):
    return {
        "id": post_id,
        "title": f"Completely Updated Post {post_id}",
        "body": f"Full update for post {post_id} performed successfully.",
        "userId": 1
    }

def patch_post_payload(post_id):
    return {
        "title": f"Patched Title {post_id}"
    }
