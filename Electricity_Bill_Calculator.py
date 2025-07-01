# ⚡ Electricity Bill Calculator using Python
# 📜 Criteria:
# - First 100 units: No charge
# - Next 100 units (101 to 200): ₹5 per unit
# - Beyond 200 units: ₹10 per unit

def bill():
    print("🔌 Welcome to the Electricity Bill Calculator 💡")
    print("\n📄 Billing Rules:")
    print("• First 100 units  No charge")
    print("• Next 100 units (101-200)  ₹5 per unit")
    print("• Above 200 units  ₹10 per unit\n")

    try:
        units = int(input("🔢 Enter the number of units used: "))
        
        if units >= 0:
            print("🧮 Calculating your bill...")

            if units <= 100:
                amount = 0
                print("✅ No charge for the first 100 units.")
                print(f"💰 Total Bill Amount: ₹{amount}")
            
            elif units <= 200:
                amount = (units - 100) * 5
                print(f"💰 Chargeable Units: {units - 100} units @ ₹5/unit")
                print(f"💰 Total Bill Amount: ₹{amount}")
            
            else:
                charge_5 = 100 * 5     # ₹5 for 101-200
                charge_10 = (units - 200) * 10
                amount = charge_5 + charge_10
                print(f"💰 Chargeable Units: 100 units @ ₹5 = ₹{charge_5}")
                print(f"💰 Extra Units: {units - 200} units @ ₹10 = ₹{charge_10}")
                print(f"💰 Total Bill Amount: ₹{amount}")

        else:
            print("⚠️ Invalid input! Units cannot be negative.")

    except ValueError:
        print("⚠️ Please enter a valid number (digits only).")

# 🧾 Calling the bill function
bill()
