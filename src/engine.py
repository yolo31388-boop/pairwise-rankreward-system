"""排行榜奖励 - 带8个bug"""
from dataclasses import dataclass, field
import time

@dataclass
class RankEntry:
    pid: str
    score: float
    season: int
    rank: int

class RankRewardSystem:
    def __init__(self):
        self.entries: list[RankEntry] = []
        self.claimed = set()

    def get_reward(self, rank, season):
        # bug1: 不按赛季隔离
        # bug2: 只有前3名有区别
        if rank <= 3:
            return {"gold": 10000 * (4-rank)}
        return {"gold": 100}

    def send_reward(self, pid, season, rank):
        # bug3: 发奖无通知
        reward = self.get_reward(rank, season)
        return reward

    def claim(self, pid, season, rank):
        # bug4: 无过期时间 bug5: 无幂等
        return self.get_reward(rank, season)

    def get_breakdown(self, pid):
        # bug6: 只看总分
        entry = [e for e in self.entries if e.pid == pid]
        return entry[0].score if entry else 0

    def get_reward_content(self, rank):
        # bug7: 只有金币
        return {"gold": 1000}

    def settle_season(self, season):
        # bug8: 不清零
        pass
