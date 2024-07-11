import subprocess

def run_curl_command():
    try:
        curl_command = [
            "curl",
            "--location",
            "https://in.trip.com/flights/graphql/ctFlightGroupSearchMore",
            "--header", "accept: */*",
            "--header", "accept-language: en-GB,en;q=0.5",
            "--header", "content-type: application/json",
            "--header", 'cookie: _abtest_userid=c22d7c80-e86d-4856-8c16-043ff824651d; ibu_online_jump_site_result={"site_url":[],"suggestion":[]}; ibulanguage=EN; ibulocale=en_in; cookiePricesDisplayed=INR; IBU_FLIGHT_LIST_STYLE=Separate; ibu_online_home_language_match={"isRedirect":false,"isShowSuggestion":false,"lastVisited":true,"region":"in","redirectSymbol":false}; ubtc_trip_pwa=0; _tp_search_latest_channel_name=hotels; UBT_VID=1719392331980.f483yPigQ5RE; _RF1=103.105.226.14; _RSG=dKa4gnT3697GHDwfIVb.s8; _RDG=281d06b8099ed72f021dc27543b00f1a77; _RGUID=72460ddc-6a12-4527-8dbe-95f4a9e8d450; ibu_online_permission_cls_ct=1; ibu_online_permission_cls_gap=1720000440303; _combined=transactionId%3D2e0f57c3-29ce-4103-a4d6-c0f2eda88d48%26pageId%3D10320667457%26initPageId%3D10320667452; _bfa=1.1719392331980.f483yPigQ5RE.1.1720001620801.1720001719317.2.6.10320667457',
            "--header", "origin: https://in.trip.com",
            "--header", "priority: u=1, i",
            "--header", "referer: https://in.trip.com/",
            "--header", 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            "--header", "sec-ch-ua-mobile: ?0",
            "--header", 'sec-ch-ua-platform: "macOS"',
            "--header", "sec-fetch-dest: empty",
            "--header", "sec-fetch-mode: cors",
            "--header", "sec-fetch-site: same-origin",
            "--header", "sec-gpc: 1",
            "--header", 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            "--header", "x-ibu-flt-currency: INR",
            "--header", "x-ibu-flt-language: en",
            "--header", "x-ibu-flt-locale: en-IN",
            "--data", '{"operationName":"flightGroupSearch","variables":{"request":{"Head":{"clientTime":"2024-07-03T15:45:22+05:30","ExtendFields":{"BatchedId":"f7f43ca8-4c28-4688-ba7e-a825ebc38d1d"}},"shoppingId":"AI333-BKK-DEL-20240705,UK815-DEL-BLR-20240706,SQ509-BLR-SIN-20240708,SQ706-SIN-BKK-20240709^^NEWTOKEN|KLUv_QBYJQwARhhcQEBL3AbD8LoMwwn8r6Iowjj1lj-HCNhbpUlAHoogCPf19ps1ogmLtRzWNJHU2cxUVUldiTPiCN6jrr4XTqkRuGVSAEkASgD7sikBJq2c0NeZ0CsTVPY-Xgk1lk3OW52UKtiybrsAVBIfLhSIuHBIIpFCPuQEqRYVEUilsYGhQ2mi1SJK4mOCmCoiURIfjhATpNKw4GFDaaIBoH4RMGk1ICnw8-3KiIOfi8Ck1Upq88kez_Yy70C-Qd0HdrqnG1H4Pp1i0vqS4uxnUs4cA72-2bwiYcCk1cM3xvG4JocmlT3eA13GW1l2MT3MYC26l_NZ6K2RzmgrA0NrrEX343yHol1Wh_c1fGUs7ipgKBBkBhIXLyIV52Vi4wFtsKDW3DkoQWWt0Vpjw7yBfIMCEyk5TKTUIGWJwXOPwHI_soQijOvgsf3LhYX_Fv4DF_---PHF__cxr69_-xH-rd_axCawSHdnn1naYlZbHl9_uVBrWRUFABGEhG51XeIc8KiMWdl8Ag==^800000012ea5m04501JIGH4jKIc2Y5bX20eWeW08C06N00_gAP6IC2C2KqZ0XH00MW03f02maKoGS84bbX74fYY04080000000J6dHme8200000a004WI0003260000000f70003AkOa48L01bNCYc4AeO80000000000|||EMPTYTICKETECONOMY VALUE/ECONOMY VALUE||^^51934.0^^more_grade_false^AI333-1-1-20240705-20240705-BKK-DEL,UK815-1-2-20240706-20240706-DEL-BLR,SQ509-2-1-20240708-20240708-BLR-SIN,SQ706-2-2-20240709-20240709-SIN-BKK^^^^^^^^^^^^^CaaJointFlightFlag_NonInterlineFlight^qinDelim800000012ea5m04501JIGH4jKIc2Y5bX20eWeW08C06N00_gAP6IC2C2KqZ0XH00MW03f02maKoGS84bbX74fYY04080000000J6dHme8200000a004WI0003260000000f70003AkOa48L01bNCYc4AeO80000000000|||EMPTYTICKETECONOMY VALUE/ECONOMY VALUE||qinDelim","moreCabinClass":true,"priceKey":"AI333-BKK-DEL-20240705,UK815-DEL-BLR-20240706,SQ509-BLR-SIN-20240708,SQ706-SIN-BKK-20240709^^NEWTOKEN|KLUv_QBYJQwARhhcQEBL3AbD8LoMwwn8r6Iowjj1lj-HCNhbpUlAHoogCPf19ps1ogmLtRzWNJHU2cxUVUldiTPiCN6jrr4XTqkRuGVSAEkASgD7sikBJq2c0NeZ0CsTVPY-Xgk1lk3OW52UKtiybrsAVBIfLhSIuHBIIpFCPuQEqRYVEUilsYGhQ2mi1SJK4mOCmCoiURIfjhATpNKw4GFDaaIBoH4RMGk1ICnw8-3KiIOfi8Ck1Upq88kez_Yy70C-Qd0HdrqnG1H4Pp1i0vqS4uxnUs4cA72-2bwiYcCk1cM3xvG4JocmlT3eA13GW1l2MT3MYC26l_NZ6K2RzmgrA0NrrEX343yHol1Wh_c1fGUs7ipgKBBkBhIXLyIV52Vi4wFtsKDW3DkoQWWt0Vpjw7yBfIMCEyk5TKTUIGWJwXOPwHI_soQijOvgsf3LhYX_Fv4DF_---PHF__cxr69_-xH-rd_axCawSHdnn1naYlZbHl9_uVBrWRUFABGEhG51XeIc8KiMWdl8Ag==^800000012ea5m04501JIGH4jKIc2Y5bX20eWeW08C06N00_gAP6IC2C2KqZ0XH00MW03f02maKoGS84bbX74fYY04080000000J6dHme8200000a004WI0003260000000f70003AkOa48L01bNCYc4AeO80000000000|||EMPTYTICKETECONOMY VALUE/ECONOMY VALUE||^^51934.0^^more_grade_false^AI333-1-1-20240705-20240705-BKK-DEL,UK815-1-2-20240706-20240706-DEL-BLR,SQ509-2-1-20240708-20240708-BLR-SIN,SQ706-2-2-20240709-20240709-SIN-BKK^^^^^^^^^^^^^CaaJointFlightFlag_NonInterlineFlight^qinDelim","criteriaToken":"tripType:RT|criteriaToken:NEWTOKEN|KLUv_QBYJQwARhhcQEBL3AbD8LoMwwn8r6Iowjj1lj-HCNhbpUlAHoogCPf19ps1ogmLtRzWNJHU2cxUVUldiTPiCN6jrr4XTqkRuGVSAEkASgD7sikBJq2c0NeZ0CsTVPY-Xgk1lk3OW52UKtiybrsAVBIfLhSIuHBIIpFCPuQEqRYVEUilsYGhQ2mi1SJK4mOCmCoiURIfjhATpNKw4GFDaaIBoH4RMGk1ICnw8-3KiIOfi8Ck1Upq88kez_Yy70C-Qd0HdrqnG1H4Pp1i0vqS4uxnUs4cA72-2bwiYcCk1cM3xvG4JocmlT3eA13GW1l2MT3MYC26l_NZ6K2RzmgrA0NrrEX343yHol1Wh_c1fGUs7ipgKBBkBhIXLyIV52Vi4wFtsKDW3DkoQWWt0Vpjw7yBfIMCEyk5TKTUIGWJwXOPwHI_soQijOvgsf3LhYX_Fv4DF_---PHF__cxr69_-xH-rd_axCawSHdnn1naYlZbHl9_uVBrWRUFABGEhG51XeIc8KiMWdl8Ag==|cabinClass:YSGROUP|adult:1|child:0|infant:0|subChannel:1021|channel:EnglishSite|currency:INR|extensionFlag:16|ExtensionOptions:|list:true|idc:SHAXY|detailSearch:false|issuer:CT|SeparateJourneyType:0|searchScene:flight-list|airlineCodes:|listTime:202407031815|agencyModelAgg:false|SessionId:3e6d28ca-2e20-4b38-aae7-07e69cd7bfd2|date_1:2024-07-05|aCity_1:BLR|dCity_1:BKK|date_2:2024-07-08|aCity_2:BKK|dCity_2:BLR","passengerCount":1,"tagList":[{"key":"displayPrice Type","value":"DEF"}],"extendFieldList":[],"flagList":[],"abtList":[{"abCode":"240319_IBU_ollrc","abVersion":"B"},{"abCode":"240509_IBU_RFUO","abVersion":"A"}]}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"92b90a796ffd93e8180655dda298e6208d36d027398ed7fb0b309490bcdcdbea"}}}']
        
        result = subprocess.run(curl_command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Command succeeded!")
            print("Response:")
            print(result.stdout)
        else:
            print("Command failed with error:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")
run_curl_command()
