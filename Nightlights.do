import excel "C:\Users\elisa\OneDrive\Desktop\Night lights\NightLights Sum by Country Year.xlsx", sheet("Sheet1") firstrow
reshape long year, i(ISO3) j(annual)
rename year nightlights
rename annual year

