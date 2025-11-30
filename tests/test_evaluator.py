import unittest
import os
import sys
import yaml

# Add project root to path so we can import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.data_agent import DataAgent
from src.utils.llm_client import LLMClient

class TestKasparroAnalyst(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test."""
        # Load real config
        with open("config/config.yaml", "r") as f:
            self.config = yaml.safe_load(f)
            
        # Point to the sample data for testing (or real data if sample missing)
        self.config['data']['path'] = "data/synthetic_fb_ads_undergarments.csv"

    def test_data_loading(self):
        """Test if DataAgent loads and cleans data correctly."""
        agent = DataAgent(self.config)
        df = agent.load_and_clean()
        
        self.assertFalse(df.empty, "Dataframe should not be empty")
        self.assertIn("roas", df.columns, "ROAS column should be calculated")
        
        # Check if ROAS is actually calculated (not all zeros)
        mean_roas = df['roas'].mean()
        self.assertGreater(mean_roas, 0, "Mean ROAS should be positive")

    def test_performance_summary(self):
        """Test if the summary dictionary has the right keys."""
        agent = DataAgent(self.config)
        agent.load_and_clean()
        summary = agent.get_performance_summary()
        
        required_keys = ['current_roas', 'previous_roas', 'spend_change_percent']
        for key in required_keys:
            self.assertIn(key, summary)

    def test_llm_connection(self):
        """Check if LLM client initializes (Mock or Real)."""
        client = LLMClient(self.config)
        self.assertIsNotNone(client, "LLM Client should initialize")

if __name__ == '__main__':
    unittest.main()