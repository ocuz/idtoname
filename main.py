import aiohttp,asyncio

API="https://users.roblox.com/v1/users"
WEBHOOK="https://discord.com/api/webhooks/1372648911375769691/2BTmnK9tsgQo5IMNIf9Stbtu7JHbVRK2JS7wV1KIVcvKpHteNETKRM6ohKW0LT74MQo"
ids=open("ids.txt").read().splitlines()

async def fetch(s,uid):
    while True:
        try:
            r=await s.get(f"{API}/{uid}")
            if r.status==200:
                d=await r.json()
                if d:
                    out=f"{uid}-{d['name']}"
                    open("usernames.txt","a").write(out+"\n");print(out);return
                open("inexistant.txt","a").write(uid+"\n")
                await s.post(WEBHOOK,json={"content":uid});return
            if r.status==429: await asyncio.sleep(3);continue
            return
        except: await asyncio.sleep(3)

async def main():
    async with aiohttp.ClientSession() as s:
        for uid in ids: await fetch(s,uid);await asyncio.sleep(.1)

asyncio.run(main())
