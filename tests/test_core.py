import unittest
from sentinelforge.modules.common import validate_host
from sentinelforge.modules.password_audit import estimate_password
from sentinelforge.modules.recon import plan
from sentinelforge.core.scope import Scope, require_authorized


class TestCore(unittest.TestCase):
    def test_valid_host(self):
        self.assertEqual(validate_host("example.com"),"example.com")
    def test_reject_url(self):
        with self.assertRaises(ValueError): validate_host("https://example.com")
    def test_password_empty(self):
        self.assertEqual(estimate_password("")["score"],0)
    def test_password_longer_scores_higher(self):
        self.assertGreater(estimate_password("LongerPassword123!")["entropy_bits"], estimate_password("abc")["entropy_bits"])
    def test_recon_plan(self):
        self.assertEqual(plan("example.com")["target"],"example.com")
    def test_scope_gate(self):
        with self.assertRaises(PermissionError): require_authorized(Scope("localhost",False))
        require_authorized(Scope("localhost",True))
if __name__=="__main__": unittest.main()
