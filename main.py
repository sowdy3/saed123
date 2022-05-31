import asyncio
from pytgcalls import idle
from driver.veez import call_py, bot

async def mulai_bot():
    print("تم تشغيل البوت")
    await bot.start()
    print("اذهب لتحقق من البوت")
    await call_py.start()
    await idle()
    await pidle()
    print("تم تفعيل البوت بنجاح")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
