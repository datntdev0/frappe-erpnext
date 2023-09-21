# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from frappe import _

def get():
	return {
		_("ASSETS"): {
			_("Cash on hand"): {
				_("Vietnamese dong"): { "account_number": "1111" },
				_("Foreign currencies"): { "account_number": "1112" },
				_("Monetary Gold"): { "account_number": "1113" },
				"account_number": "111",
				"account_type": "Cash",
			},
			_("Cash in banks"): {
				_("Vietnamese dong"): { "account_number": "1121" },
				_("Foreign currencies"): {  "account_number": "1122" },
				_("Monetary Gold"): { "account_number": "1123" },
				"account_number": "112",
				"account_type": "Bank",
			},
			_("Cash in transit"): {
				_("Vietnamese dong"): { "account_number": "1131" },
				_("Foreign currencies"): {  "account_number": "1132" },
				"account_number": "113",
			},
			_("Trading Securities"): {
				_("Shares"): { "account_number": "1211" },
				_("Bonds"): { "account_number": "1212" },
				_("Securities and other financial instrusments"): { "account_number": "1218" },
				"account_number": "121",
			},
			_("Investments held to maturity"): {
				_("Time deposits"): { "account_number": "1281" },
				_("Bonds"): { "account_number": "1282" },
				_("Loan"): { "account_number": "1283" },
				_("Other investments held to maturity"): { "account_number": "1288" },
				"account_number": "128",
			},
			_("Trade Receivables"): { "account_number": "131", },
			_("Deductible VAT"): {
				_("Deductible VAT of goods and services"): { "account_number": "1331" },
				_("Deductible VAT of fixed assets"): { "account_number": "1332" },
				"account_number": "133",
			},
			_("Internal Receivables"): {
				_("Working capital provided to sub-units"): { "account_number": "1361" },
				_("Internal Receivables on foreign exchange diff"): { "account_number": "1362" },
				_("Internal Receivables on borrowing cost eligible for capitalization"): { "account_number": "1363" },
				_("Other internal receivables"): { "account_number": "1368" },
				"account_number": "136",
			},
			_("Other receivables"): {
				_("Shortage of assets awaiting resolution"): { "account_number": "1381" },
				_("Privatization receivables"): { "account_number": "1385" },
				_("Other receivables"): { "account_number": "1388" },
				"account_number": "138",
			},
			_("Advances"): { "account_number": "141" },
			_("Goods in transit"): { "account_number": "151" },
			_("Raw materials"): { "account_number": "152" },
			_("Tools & supplies"): {
				_("Tools & supplies"): { "account_number": "1531" },
				_("Packaging rotation"): { "account_number": "1532" },
				_("Instrument for rent"): { "account_number": "1533" },
				_("Equipment & spare parts"): { "account_number": "1534" },
				"account_number": "153",
			},
			_("Work in process"): { "account_number": "154" },
			_("Finished products"): {
				_("Finished products"): { "account_number": "1551" },
				_("Real estate finished goods"): { "account_number": "1557" },
				"account_number": "155",
			},
			_("Merchandise goods"): {
				_("Purchase costs"): { "account_number": "1561" },
				_("Incidental expense"): { "account_number": "1562" },
				_("Property Inventories"): { "account_number": "1567" },
				"account_number": "156",
			},
			_("Outward goods on consignment"): { "account_number": "157" },
			_("Goods in bonded warehouse"): { "account_number": "158" },
			_("Finished products"): {
				_("Previous years expenditure"): { "account_number": "1611" },
				_("Current years expenditure"): { "account_number": "1612" },
				"account_number": "161",
			},
			_("Government bonds purchase-resale"): { "account_number": "171" },
			_("Tangible fixed assets"): {
				_("Building & structures"): { "account_number": "2111" },
				_("Machinery & Equipment"): { "account_number": "2112" },
				_("Transportation & transmission vehicles "): { "account_number": "2113" },
				_("Office equipment"): { "account_number": "2114" },
				_("Perenial trees, working and producing animals"): { "account_number": "2115" },
				_("Other tangible fixed assets"): { "account_number": "2118" },
				"account_number": "211",
			},
			_("Financial leased assets"): {
				_("Financial leased tangible assets"): { "account_number": "2121" },
				_("Financial leased intangible assets"): { "account_number": "2122" },
				"account_number": "212",
			},
			_("Intangible fixed assets"): {
				_("Land use right"): { "account_number": "2131" },
				_("Copyrights"): { "account_number": "2132" },
				_("Patents"): { "account_number": "2133" },
				_("Trademarks and brand name"): { "account_number": "2134" },
				_("Computer Software"): { "account_number": "2135" },
				_("License & franchises"): { "account_number": "2136" },
				_("Other intangible fixed assets"): { "account_number": "2138" },
				"account_number": "213",
			},
			_("Depreciation of fixed assets"): {
				_("Depreciation of tangible fixed assets"): { "account_number": "2141" },
				_("Depreciation of financial leased assets"): { "account_number": "2142" },
				_("Depreciation of intangible fixed assets"): { "account_number": "2143" },
				_("Depreciation of investment properties "): { "account_number": "2147" },
				"account_number": "214",
			},
			_("Investment properties"): { "account_number": "217" },
			_("Investment in subsidiaries"): { "account_number": "221" },
			_("Investment in Joint venture and associates"): { "account_number": "222" },
			_("Other investments"): {
				_("Equipty investment in other entity"): { "account_number": "2281" },
				_("Other investment"): { "account_number": "2288" },
				"account_number": "228",
			},
			_("Allowance for impairment of assets"): {
				_("Allowance for decline in value of trading securities"): { "account_number": "2291" },
				_("Allowance for investment loss in other entity"): { "account_number": "2292" },
				_("Allowance for doubtful debt"): { "account_number": "2293" },
				_("Inventory reserve"): { "account_number": "2294" },
				"account_number": "229",
			},
			_("Construction in progress"): {
				_("Acquisition of Fixed assets"): { "account_number": "2411" },
				_("Construction in progress"): { "account_number": "2412" },
				_("Extra-ordinary repair of fixed assets "): { "account_number": "2413" },
				"account_number": "241",
			},
			_("Prepaid expenses"): { "account_number": "242" },
			_("Deffered tax assets"): { "account_number": "243" },
			_("Mortgage, collaterals and deposits"): { "account_number": "244" },
		},
		_("LIABILITIES"): {
			_("Trade Payables"): { "account_number": "331" },
			_("Taxes and other payable to State Budget"): {
				_("Value Added Tax (VAT)"): { 
					_("VAT output"): { "account_number": "33311" },
					_("VAT on imported goods"): { "account_number": "33312" },
					"account_number": "3331" 
				},
				_("Special consumption tax"): { "account_number": "3332" },
				_("Import & export duties"): { "account_number": "3333" },
				_("Corporate Income Tax"): { "account_number": "3334" },
				_("Personal income tax"): { "account_number": "3335" },
				_("Natural resources using tax"): { "account_number": "3336" },
				_("Land & housing tax, land rental charges"): { "account_number": "3337" },
				_("Environment protection tax and other taxes"): { 
					_("Environment protection tax"): { "account_number": "33381" },
					_("Other taxes"): { "account_number": "33382" },
					"account_number": "3338" 
				},
				_("Fee & charge & other payables"): { "account_number": "3339" },
				"account_number": "333",
			},
			_("Payable to employees"): {
				_("Payable to employees"): { "account_number": "3341" },
				_("Payable to other"): { "account_number": "3348" },
				"account_number": "334",
			},
			_("Accrued expenses"): { "account_number": "335" },
			_("Internal payables"): {
				_("Internal payables for working capital received"): { "account_number": "3361" },
				_("Internal payables for foreign exchange diff"): { "account_number": "3362" },
				_("Internal payables for borrowing cost eligible for capitalization"): { "account_number": "3363" },
				_("Other internal payables"): { "account_number": "3368" },
				"account_number": "336",
			},
			_("Progress billings for contruction contract"): { "account_number": "337" },
			_("Other payables"): {
				_("Surplus of assets awaiting for resolution"): { "account_number": "3381" },
				_("Trade Union fees"): { "account_number": "3382" },
				_("Social insurance"): { "account_number": "3383" },
				_("Health insurance"): { "account_number": "3384" },
				_("Privatization payable"): { "account_number": "3385" },
				_("Unemployment insurance"): { "account_number": "3386" },
				_("Unearned revenue"): { "account_number": "3387" },
				_("Others"): { "account_number": "3388" },
				"account_number": "338",
			},
			_("Borrowings and finance lease liabilities"): {
				_("Borrowings"): { "account_number": "3411" },
				_("Finance lease liabilities"): { "account_number": "3412" },
				"account_number": "341",
			},
			_("Issued bonds"): {
				_("Ordinary bonds"): { 
					_("Par value of bonds"): { "account_number": "34311" },
					_("Bond discounts"): { "account_number": "34312" },
					_("Bond premiums"): { "account_number": "34313" },
					"account_number": "3431" 
				},
				_("Convertible bonds"): { "account_number": "3432" },
				"account_number": "343",
			},
			_("Deposits received"): { "account_number": "344" },
			_("Deferred tax liablilities"): { "account_number": "347" },
			_("Provisions payables"): {
				_("Product warranty provisions"): { "account_number": "3521" },
				_("Construction warranty provisions"): { "account_number": "3522" },
				_("Enterprise restructuring provisions"): { "account_number": "3523" },
				_("Other provisions"): { "account_number": "3524" },
				"account_number": "352",
			},
			_("Bonus and welfare fund"): {
				_("Bonus fund"): { "account_number": "3531" },
				_("Welfare fund"): { "account_number": "3532" },
				_("Welfare fund used for fixed asset acquisitions "): { "account_number": "3533" },
				_("Management bonus fund"): { "account_number": "3534" },
				"account_number": "353",
			},
			_("Science and technology development fund"): {
				_("Science and technology development fund"): { "account_number": "3561" },
				_("Science and technology development fund used for fixed asset acquisition"): { "account_number": "3562" },
				"account_number": "356",
			},
			_("Price stabilization fund"): { "account_number": "357" },
		},
		_("OWNER'S EQUITY"): {
			_("Owner’s equity"): {
				_("Contributed capital"): { 
					_("Ordinary shares with voting rights"): { "account_number": "41111" },
					_("Preference shares "): { "account_number": "41112" },
					"account_number": "4111" 
				},
				_("Capital surplus"): { "account_number": "4112" },
				_("Conversion options on convertible bonds"): { "account_number": "4113" },
				_("Other capital"): { "account_number": "4118" },
				"account_number": "411",
			},
			_("Revaluation differences on asset"): { "account_number": "412" },
			_("Foreign exchange differences"): {
				_("Exchange rate differences on revaluation of monetary items denominated in foreign currency"): { "account_number": "4131" },
				_("Exchange rate differences in preoperating period"): { "account_number": "4132" },
				"account_number": "413",
			},
			_("Investment & development funds"): { "account_number": "414" },
			_("Enterprise reorganization assistance fund"): { "account_number": "417" },
			_("Other equity funds"): { "account_number": "418" },
			_("Treasury stocks"): { "account_number": "419" },
			_("Undistributed profit after tax"): {
				_("Undistributed profit after tax of previous year"): { "account_number": "4211" },
				_("Undistributed profit after tax of current year"): { "account_number": "4212" },
				"account_number": "421",
			},
			_("Capital expenditure funds"): { "account_number": "441" },
			_("Government sourced funds"): {
				_("Government sourced funds of previous year"): { "account_number": "4611" },
				_("Government sourced funds of current year"): { "account_number": "4612" },
				"account_number": "461",
			},
			_("Non-business funds used for fixed asset acquisitions"): { "account_number": "466" },
		}, 
		_("REVENUE"): {
			_("Revenues"): { 
				_("Revenue from sales of merchandises"): { "account_number": "5111" },
				_("Revenue from sales of finished goods"): { "account_number": "5112" },
				_("Revenue from services rendered"): { "account_number": "5113" },
				_("Revenue from government grants"): { "account_number": "5114" },
				_("Revenue from investment properties"): { "account_number": "5117" },
				_("Other revenue"): { "account_number": "5118" },
				"account_number": "511" 
			},
			_("Financial income"): { "account_number": "515" },
			_("Revenue deductions"): { 
				_("Sales discounts"): { "account_number": "5211" },
				_("Sales allowances"): { "account_number": "5212" },
				_("Sales returns"): { "account_number": "5213" },
				"account_number": "521" 
			},
		},
		_("COST OF PRODUCTION & BUSINESS"): {
			_("Purchases"): { 
				_("Raw material purchases"): { "account_number": "6111" },
				_("Goods purchases"): { "account_number": "6112" },
				"account_number": "611" 
			},
			_("Direct raw materials costs"): { "account_number": "621" },
			_("Direct labor costs"): { "account_number": "622" },
			_("Costs of construction machinery"): { 
				_("Labor cost"): { "account_number": "6231" },
				_("Material cost"): { "account_number": "6232" },
				_("Tools and instruments"): { "account_number": "6233" },
				_("Depreciation expense"): { "account_number": "6234" },
				_("Outside services"): { "account_number": "6237" },
				_("Other expenses"): { "account_number": "6238" },
				"account_number": "623" 
			},
			_("Production overheads"): { 
				_("Factory staff costs"): { "account_number": "6271" },
				_("Material cost"): { "account_number": "6272" },
				_("Tools and instruments"): { "account_number": "6273" },
				_("Fixed asset depreciation"): { "account_number": "6274" },
				_("Outside services"): { "account_number": "6277" },
				_("Other expenses"): { "account_number": "6278" },
				"account_number": "627" 
			},
			_("Production costs"): { "account_number": "631" },
			_("Costs of goods sold"): { "account_number": "632" },
			_("Financial expenses"): { "account_number": "635" },
			_("Selling expenses"): { 
				_("Employees costs"): { "account_number": "6411" },
				_("Materials and packing materials"): { "account_number": "6412" },
				_("Tools and instruments"): { "account_number": "6413" },
				_("Fixed asset depreciation"): { "account_number": "6414" },
				_("Warranty expenses"): { "account_number": "6415" },
				_("Outside services"): { "account_number": "6417" },
				_("Other costs"): { "account_number": "6418" },
				"account_number": "641" 
			},
			_("General & administration expenses"): { 
				_("Employees cost"): { "account_number": "6421" },
				_("Office supply expenses"): { "account_number": "6422" },
				_("Stationery cost"): { "account_number": "6423" },
				_("Fixed asset depreciation"): { "account_number": "6424" },
				_("Taxes, fees, charges"): { "account_number": "6425" },
				_("Provision expenses"): { "account_number": "6426" },
				_("Outside services"): { "account_number": "6427" },
				_("Other costs"): { "account_number": "6428" },
				"account_number": "642" 
			},
		},
		_("OTHER INCOME"): {
			_("Other income"): { "account_number": "711" },
		},
		_("OTHER EXPENSES"): {
			_("Other expenses"): { "account_number": "811" },
			_("Income tax expenses"): { 
				_("Current tax expenses"): { "account_number": "8211" },
				_("Deferred tax expenses"): { "account_number": "8212" },
				"account_number": "821" 
			},
		},
		_("INCOME SUMMARY"): {
			_("Income Summary"): { "account_number": "911" },
		}
	}
