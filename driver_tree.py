from graphviz import Digraph

def create_driver_tree():
    driver_tree = Digraph("DriverTree", format="png")
    driver_tree.attr(rankdir="TB", size="8,8")
    driver_tree.attr("node", shape="box", style="rounded, filled", color="lightblue", fontname="Arial")

    driver_tree.node("MainIssue", "Parent Concerns About Youth Sports Program")
    driver_tree.node("InjuryReporting", "Injury Reporting")
    driver_tree.node("ConcussionTraining", "Concussion Training")
    driver_tree.node("CommunicationRules", "Communication of Rules")
    driver_tree.node("RefereeTraining", "Referee Training")
    driver_tree.node("MWRStaffOversight", "MWR Staff Oversight")

    driver_tree.edges([
        ("MainIssue", "InjuryReporting"),
        ("MainIssue", "ConcussionTraining"),
        ("MainIssue", "CommunicationRules"),
        ("MainIssue", "RefereeTraining"),
        ("MainIssue", "MWRStaffOversight")
    ])

    driver_tree.node("ProperDocumentation", "Proper Documentation")
    driver_tree.node("FollowUpCommunication", "Follow-Up Communication")
    driver_tree.edges([
        ("InjuryReporting", "ProperDocumentation"),
        ("InjuryReporting", "FollowUpCommunication")
    ])

    driver_tree.node("ConsistencyDelivery", "Consistency in Delivery")
    driver_tree.node("ParentAwareness", "Parent Awareness")
    driver_tree.edges([
        ("ConcussionTraining", "ConsistencyDelivery"),
        ("ConcussionTraining", "ParentAwareness")
    ])

    driver_tree.node("UniformDistribution", "Uniform Distribution Across Teams")
    driver_tree.node("ClarityParentsCoaches", "Clarity for Parents and Coaches")
    driver_tree.edges([
        ("CommunicationRules", "UniformDistribution"),
        ("CommunicationRules", "ClarityParentsCoaches")
    ])

    driver_tree.node("KnowledgeIFABRules", "Knowledge of IFAB Rules")
    driver_tree.node("ConsistentEnforcement", "Consistent Enforcement")
    driver_tree.edges([
        ("RefereeTraining", "KnowledgeIFABRules"),
        ("RefereeTraining", "ConsistentEnforcement")
    ])

    driver_tree.node("ProactiveMonitoring", "Proactive Monitoring")
    driver_tree.node("Accountability", "Accountability")
    driver_tree.edges([
        ("MWRStaffOversight", "ProactiveMonitoring"),
        ("MWRStaffOversight", "Accountability")
    ])

    driver_tree.render("DriverTree")

create_driver_tree()