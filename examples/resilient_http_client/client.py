import asyncio
import random
import logging
import httpx

logger = logging.getLogger("resilient_client")

class ResilientClient:
    """Production-grade resilient async HTTP client with jittered backoff and bounded concurrency."""
    def __init__(self, base_url: str, max_concurrent: int = 5):
        self.base_url = base_url
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.session = None

    async def __aenter__(self):
        self.session = httpx.AsyncClient(base_url=self.base_url)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session and not self.session.is_closed:
            await self.session.aclose()

    async def fetch(self, endpoint: str, max_retries: int = 3):
        async with self.semaphore:
            for attempt in range(1, max_retries + 1):
                try:
                    response = await self.session.get(endpoint)
                    if response.status_code in (429, 500, 502, 503, 504):
                        wait_time = (2 ** attempt) + random.uniform(0.1, 0.5)
                        logger.warning("retryable_error", extra={"status": response.status_code, "attempt": attempt, "wait": wait_time})
                        await asyncio.sleep(wait_time)
                        continue
                    response.raise_for_status()
                    return response.json()
                except httpx.RequestError as exc:
                    if attempt == max_retries:
                        logger.error("max_retries_exceeded", extra={"error": str(exc), "endpoint": endpoint})
                        raise
                    wait_time = (2 ** attempt) + random.uniform(0.1, 0.5)
                    await asyncio.sleep(wait_time)
