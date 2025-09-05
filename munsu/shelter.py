import asyncio
from playwright.async_api import async_playwright
import pandas as pd


async def shelter(city_name="서울특별시"):
    url = "https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/htw/htweaiList.html?menuSeq=862"
    all_data = []

    # 시도명 -> select value 매핑
    city_value_map = {
        "서울특별시": "11",
        "부산광역시": "26",
        "대구광역시": "27",
        "인천광역시": "28",
        "광주광역시": "29",
        "대전광역시": "30",
        "울산광역시": "31",
        "세종특별자치시": "36",
        "경기도": "41",
        "강원특별자치도": "51",
        "충청북도": "43",
        "충청남도": "44",
        "전북특별자치도": "52",
        "전라남도": "46",
        "경상북도": "47",
        "경상남도": "48",
        "제주특별자치도": "50"
    }

    value = city_value_map.get(city_name, "11")  # 기본 서울

    try:
        async with async_playwright() as p:
            browser = await getattr(p, "firefox").launch(headless=False, slow_mo=200)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(url)

            # 도시 선택
            await page.select_option("select#sbLawArea1", value)
            await page.select_option("select#usePsblDiv","누구나 이용가능")

            # 검색 버튼 클릭
            buttons = page.locator("a.search_btn")
            await buttons.nth(1).click()

            page_num = 1
            while True:
                print(f"{city_name} - 현재 {page_num} 페이지 크롤링 중...")
                await page.wait_for_selector("table tbody tr")
                rows = await page.locator("table tbody tr").all()
                for row in rows:
                    cols = await row.locator("td").all_inner_texts()
                    all_data.append(cols)

                next_button = page.locator("#apagenext")
                if await next_button.is_disabled():  # 버튼이 비활성화면 종료
                    break
                await next_button.click()
                await page.wait_for_selector("table tbody tr")
                page_num += 1

    except KeyboardInterrupt:
        print("크롤링 중단! 지금까지 수집한 데이터 저장...")
    finally:
        if all_data:
            df = pd.DataFrame(all_data)
            filename = f"safekorea_{city_name}_partial.xlsx"
            df.to_excel(filename, index=False)
            print(f"{filename} 저장 완료!")

    await browser.close()


if __name__ == "__main__":
    #asyncio.run(shelter("광주광역시"))
    #asyncio.run(shelter("대전광역시"))
    #asyncio.run(shelter("울산광역시"))
    #asyncio.run(shelter("경기도"))
    #asyncio.run(shelter("강원특별자치도"))
    #asyncio.run(shelter("충청북도"))
    #asyncio.run(shelter("충청남도"))
    #asyncio.run(shelter("전북특별자치도"))
    #asyncio.run(shelter("전라남도"))
    #asyncio.run(shelter("경상북도"))
    #asyncio.run(shelter("경상남도"))


