import aiohttp

async def post_request(url, data):
    headers = {'content-type': 'application/json', 'User-Agent': 'IOS'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=data) as resp:
            result = await resp.json()
            print(resp.request_info)
            return result
