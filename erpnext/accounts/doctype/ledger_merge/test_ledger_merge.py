# Copyright (c) 2021, Wahni Green Technologies Pvt. Ltd. and Contributors
# See license.txt

import unittest

import frappe

from erpnext.accounts.doctype.ledger_merge.ledger_merge import start_merge


class TestLedgerMerge(unittest.TestCase):
	def test_merge_success(self):
		if not frappe.db.exists("Account", "Indirect Expenses - __TC1"):
			acc = frappe.new_doc("Account")
			acc.account_name = "Indirect Expenses"
			acc.is_group = 1
			acc.parent_account = "Expenses - __TC1"
			acc.company = "__Test Company 1"
			acc.insert()
		if not frappe.db.exists("Account", "Indirect Test Expenses - __TC1"):
			acc = frappe.new_doc("Account")
			acc.account_name = "Indirect Test Expenses"
			acc.is_group = 1
			acc.parent_account = "Expenses - __TC1"
			acc.company = "__Test Company 1"
			acc.insert()
		if not frappe.db.exists("Account", "Administrative Test Expenses - __TC1"):
			acc = frappe.new_doc("Account")
			acc.account_name = "Administrative Test Expenses"
			acc.parent_account = "Indirect Test Expenses - __TC1"
			acc.company = "__Test Company 1"
			acc.insert()

		doc = frappe.get_doc(
			{
				"doctype": "Ledger Merge",
				"company": "__Test Company 1",
				"root_type": frappe.db.get_value("Account", "Indirect Test Expenses - __TC1", "root_type"),
				"account": "Indirect Expenses - __TC1",
				"merge_accounts": [
					{"account": "Indirect Test Expenses - __TC1", "account_name": "Indirect Expenses"}
				],
			}
		).insert(ignore_permissions=True)

		parent = frappe.db.get_value("Account", "Administrative Test Expenses - __TC1", "parent_account")
		self.assertEqual(parent, "Indirect Test Expenses - __TC1")

		start_merge(doc.name)

		parent = frappe.db.get_value("Account", "Administrative Test Expenses - __TC1", "parent_account")
		self.assertEqual(parent, "Indirect Expenses - __TC1")

		self.assertFalse(frappe.db.exists("Account", "Indirect Test Expenses - __TC1"))

	def test_partial_merge_success(self):
		if not frappe.db.exists("Account", "Indirect Income - __TC1"):
			acc = frappe.new_doc("Account")
			acc.account_name = "Indirect Income"
			acc.is_group = 1
			acc.parent_account = "Income - __TC1"
			acc.company = "__Test Company 1"
			acc.insert()
		if not frappe.db.exists("Account", "Indirect Test Income - __TC1"):
			acc = frappe.new_doc("Account")
			acc.account_name = "Indirect Test Income"
			acc.is_group = 1
			acc.parent_account = "Income - __TC1"
			acc.company = "__Test Company 1"
			acc.insert()
		if not frappe.db.exists("Account", "Administrative Test Income - __TC1"):
			acc = frappe.new_doc("Account")
			acc.account_name = "Administrative Test Income"
			acc.parent_account = "Indirect Test Income - __TC1"
			acc.company = "__Test Company 1"
			acc.insert()

		doc = frappe.get_doc(
			{
				"doctype": "Ledger Merge",
				"company": "__Test Company 1",
				"root_type": frappe.db.get_value("Account", "Indirect Income - __TC1", "root_type"),
				"account": "Indirect Income - __TC1",
				"merge_accounts": [
					{"account": "Indirect Test Income - __TC1", "account_name": "Indirect Test Income"},
					{"account": "Administrative Test Income - __TC1", "account_name": "Administrative Test Income"},
				],
			}
		).insert(ignore_permissions=True)

		parent = frappe.db.get_value("Account", "Administrative Test Income - __TC1", "parent_account")
		self.assertEqual(parent, "Indirect Test Income - __TC1")

		start_merge(doc.name)

		parent = frappe.db.get_value("Account", "Administrative Test Income - __TC1", "parent_account")
		self.assertEqual(parent, "Indirect Income - __TC1")

		self.assertFalse(frappe.db.exists("Account", "Indirect Test Income - __TC1"))
		self.assertTrue(frappe.db.exists("Account", "Administrative Test Income - __TC1"))

	def tearDown(self):
		for entry in frappe.db.get_all("Ledger Merge"):
			frappe.delete_doc("Ledger Merge", entry.name)

		test_accounts = [
			"Indirect Test Expenses - __TC1",
			"Administrative Test Expenses - __TC1",
			"Indirect Test Income - __TC1",
			"Administrative Test Income - __TC1",
		]
		for account in test_accounts:
			frappe.delete_doc_if_exists("Account", account)
