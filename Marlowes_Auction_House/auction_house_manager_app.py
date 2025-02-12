from Marlowes_Auction_House.artifacts.renaissance_artifact import RenaissanceArtifact
from Marlowes_Auction_House.artifacts.contemporary_artifact import ContemporaryArtifact
from Marlowes_Auction_House.collectors.museum import Museum
from Marlowes_Auction_House.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        valid_types = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}

        if artifact_type not in valid_types:
            raise ValueError("Unknown artifact type!")
        for artifact in self.artifacts:
            if artifact.name == artifact_name:
                raise ValueError(f"{artifact_name} has been already registered!")

        artifact_class = valid_types[artifact_type]
        new_artifact = artifact_class(artifact_name, artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        valid_types = {"Museum": Museum, "PrivateCollector": PrivateCollector}

        if collector_type not in valid_types:
            raise ValueError("Unknown collector type!")
        for collector in self.collectors:
            if collector.name == collector_name:
                raise ValueError(f"{collector_name} has been already registered!")

        collector_class = valid_types[collector_type]
        new_collector = collector_class(collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name), None)
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if collector.can_purchase(artifact.price, artifact.space_required):
            self.artifacts.remove(artifact)
            collector.purchased_artifacts.append(artifact)
            collector.available_money -= artifact.price
            collector.available_space -= artifact.space_required
            return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."
        else:
            return "Purchase is impossible."

    def remove_artifact(self, artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact:
            self.artifacts.remove(artifact)
            return artifact.artifact_information()
        else:
            return "No such artifact."

    def fundraising_campaigns(self, max_money: float):
        count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.available_money += collector.increase_money()
                count += 1
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        sold_count = sum(len(c.purchased_artifacts) for c in self.collectors)
        available_count = len(self.artifacts)
        collectors_info = sorted(
            self.collectors,
            key=lambda c: (-len(c.purchased_artifacts), c.name)
        )
        report = ["**Auction statistics**",
                  f"Total number of sold artifacts: {sold_count}",
                  f"Available artifacts for sale: {available_count}",
                  "***"]
        for collector in collectors_info:
            artifacts_info = ", ".join(a.name for a in collector.purchased_artifacts) or "none"
            report.append(f"Collector name: {collector.name}; Money available: {collector.available_money:.2f}; "
                          f"Space available: {collector.available_space}; Artifacts: {artifacts_info}")
        return "\n".join(report)
