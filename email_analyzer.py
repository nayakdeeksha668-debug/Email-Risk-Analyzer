
import re

print("===================================")
print("       EMAIL RISK ANALYZER")
print("===================================")

email = input("\nEnter your email message: ").lower()

risk_words = {
    "urgent": 15,
    "password": 20,
    "winner": 15,
    "click here": 20,
    "free money": 20,
    "bank account": 20,
    "verify now": 20,
    "congratulations": 10
}

detected_words = []
risk_score = 0

# Detect suspicious words
for word, points in risk_words.items():
    if word in email:
        detected_words.append(word)
        risk_score += points

# Detect links
links = re.findall(r'https?://\S+', email)

if links:
    risk_score += 20

# Keep score within 100
risk_score = min(risk_score, 100)

# Classify risk
if risk_score >= 60:
    risk_level = "HIGH"
elif risk_score >= 30:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

# Create report
report = "\n========== EMAIL RISK REPORT ==========\n"

report += "\nEmail Content:\n" + email

report += "\n\nSuspicious Words:\n"

if detected_words:
    for word in detected_words:
        report += "- " + word + "\n"
else:
    report += "None detected\n"

report += "\nLinks Found:\n"

if links:
    for link in links:
        report += "- " + link + "\n"
else:
    report += "No links found\n"

report += "\nRisk Score: " + str(risk_score) + "/100"
report += "\nRisk Level: " + risk_level

report += "\n\nAnalysis completed!"

print(report)

# Save report
with open("email_report.txt", "w") as file:
    file.write(report)

print("\nReport saved successfully!")
