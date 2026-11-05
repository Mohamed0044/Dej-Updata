from ...models import Post
from .utils import generate_ai_content

class PostNotFound(ValueError):
    pass




def _get_post_from_sum(post_id: int) -> Post:
    if type(post_id) is not int or post_id < 1:
        raise ValueError("Sorry post_id must be an integer.")

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise PostNotFound(f"Post with id {post_id} not found , try again.") from None

    if not post.content.strip():
        raise ValueError(f"Post with id {post_id} has no content to summarize,, try again.")
    return post


def _build_summary_prompt(content: str) -> str:
    return (
        "Summarize the following blog post in at most 500 characters. "
        "Return only the summary.\n\n"
        f"{content}"
    )


def summarize_post(post_id: int) -> dict:
    post = _get_post_from_sum(post_id)
    prompt = _build_summary_prompt(post.content)
    result = generate_ai_content(prompt)
    summary = result.strip()[:500].rstrip()

    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": summary,
        "length": len(summary),
    }