from datetime import datetime, timedelta

def get_user_input():
    period_days = int(input("Enter the number of period days: "))
    cycle_days = int(input("Enter the length of your menstruation cycle in days: "))
    last_period_start_date = input("Enter the start date of your last period (YYYY-MM-DD): ")
    last_period_end_date = input("Enter the end date of your last period (YYYY-MM-DD): ")
    
    return period_days, cycle_days, last_period_start_date, last_period_end_date

def calculate_next_period(last_period_start_date, cycle_days):
    last_period_start = datetime.strptime(last_period_start_date, "%Y-%m-%d").date()
    next_period_start = last_period_start + timedelta(days=cycle_days)
    
    return next_period_start

def track_menstruation_phase(cycle_day):
    if 1 <= cycle_day <= 5:
        return "Menstrual phase"
    elif 6 <= cycle_day <= 14:
        return "Follicular phase"
    elif 14 <= cycle_day <= 16:
        return "Ovulation phase"
    elif 17 <= cycle_day <= 28:
        return "Luteal phase"
    else:
        return "Invalid day"

def get_current_phase(last_period_start_date, current_date, cycle_days):
    last_period_start = datetime.strptime(last_period_start_date, "%Y-%m-%d").date()
    cycle_day = (current_date - last_period_start).days % cycle_days + 1
    
    return track_menstruation_phase(cycle_day)

def get_phase_info(phase):
    phase_info = {
        "Menstrual phase": {
            "symptoms": [
                "Cramps",
                "Fatigue",
                "Headaches",
                "Lower back pain",
                "Mood swings",
                "Breast tenderness",
                "Digestive issues",
                "Sleep disturbances"
            ],
            "food": [
                "Iron-rich foods (e.g., spinach, lentils, chickpeas, lean meats)",
                "Hydrating foods (e.g., cucumbers, watermelon, coconut water)",
                "Leafy greens (e.g., spinach, fenugreek leaves)",
                "Vitamin C-rich foods (e.g., oranges, strawberries, amla)",
                "Whole grains (e.g., oats, brown rice, whole wheat)",
                "Herbal teas (e.g., chamomile, ginger, turmeric)",
                "Dates and nuts (e.g., almonds, walnuts)"
            ],
            "exercise": [
                "Gentle yoga (e.g., Child’s Pose, Reclining Bound Angle Pose)",
                "Walking",
                "Stretching",
                "Restorative yoga",
                "Light Pilates (e.g., pelvic tilts, gentle core exercises)",
                "Tai chi",
                "Low-impact aerobic exercises",
                "Free-hand exercises (e.g., bodyweight squats, arm circles)"
            ],
            "breathing": [
                "Deep breathing exercises",
                "Meditation",
                "Diaphragmatic breathing",
                "Body scan meditation",
                "Guided imagery",
                "Progressive muscle relaxation"
            ]
        },
        "Follicular phase": {
            "symptoms": [
                "Increased energy",
                "Improved mood",
                "Heightened creativity",
                "Enhanced cognitive function",
                "Clearer skin",
                "Improved digestion"
            ],
            "food": [
                "Protein-rich foods (e.g., eggs, tofu, paneer)",
                "Healthy fats (e.g., avocados, olive oil, ghee)",
                "Fresh fruits and vegetables (e.g., apples, carrots, bell peppers)",
                "Whole grains (e.g., quinoa, barley, millets)",
                "Nuts and seeds (e.g., almonds, chia seeds, flaxseeds)",
                "Fermented foods (e.g., yogurt, kimchi, idli, dosa)"
            ],
            "exercise": [
                "Cardio (e.g., running, swimming)",
                "Strength training (e.g., weight lifting)",
                "High-intensity interval training (HIIT)",
                "Group fitness classes",
                "Cycling",
                "Outdoor activities (e.g., hiking, tennis)",
                "Pilates (e.g., reformer exercises, core strengthening)",
                "Free-hand exercises (e.g., jumping jacks, push-ups)"
            ],
            "breathing": [
                "Breath of fire",
                "Alternate nostril breathing",
                "Ujjayi breath",
                "Kapalbhati breathing",
                "Bhramari (humming bee breath)",
                "Anulom Vilom"
            ]
        },
        "Ovulation phase": {
            "symptoms": [
                "High energy",
                "Heightened senses",
                "Increased libido",
                "Ovulation pain (mittelschmerz)",
                "Optimistic mood",
                "Increased social confidence"
            ],
            "food": [
                "Anti-inflammatory foods (e.g., turmeric, ginger, garlic)",
                "Antioxidants (e.g., berries, green tea, pomegranate)",
                "Dark chocolate",
                "Omega-3 rich foods (e.g., salmon, flaxseeds, walnuts)",
                "Leafy greens (e.g., kale, Swiss chard)",
                "Hydrating foods (e.g., cucumber, coconut water)"
            ],
            "exercise": [
                "High-intensity interval training (HIIT)",
                "Dancing",
                "Running",
                "Kickboxing",
                "Bootcamp classes",
                "Sports (e.g., basketball, soccer)",
                "Pilates (e.g., advanced core workouts)",
                "Free-hand exercises (e.g., burpees, mountain climbers)"
            ],
            "breathing": [
                "Cooling breath (Sheetali)",
                "Mindfulness breathing",
                "4-7-8 breathing",
                "Chandra Bhedana",
                "Cleansing breath",
                "Visualization breathing"
            ]
        },
        "Luteal phase": {
            "symptoms": [
                "Bloating",
                "Mood swings",
                "Breast tenderness",
                "Fatigue",
                "Irritability",
                "Cravings",
                "Difficulty concentrating",
                "Sleep disturbances"
            ],
            "food": [
                "Complex carbs (e.g., sweet potatoes, whole grain pasta, brown rice)",
                "Magnesium-rich foods (e.g., dark chocolate, almonds, pumpkin seeds)",
                "Bananas",
                "Dark leafy greens (e.g., kale, spinach)",
                "Seeds (e.g., pumpkin, sunflower)",
                "Herbal teas (e.g., peppermint, chamomile)",
                "Lean proteins (e.g., fish, poultry)"
            ],
            "exercise": [
                "Light cardio (e.g., walking, gentle cycling)",
                "Stretching",
                "Yoga (e.g., Cat-Cow Pose, Legs-Up-the-Wall Pose)",
                "Swimming",
                "Low-impact aerobics",
                "Gentle strength training",
                "Pilates (e.g., gentle core stabilization)",
                "Free-hand exercises (e.g., gentle bodyweight exercises, stretching routines)"
            ],
            "breathing": [
                "Box breathing",
                "Progressive relaxation",
                "Abdominal breathing",
                "Loving-kindness meditation",
                "Guided breathwork",
                "Self-compassion meditation"
            ]
        }
    }
    return phase_info.get(phase, {})

def main():
    period_days, cycle_days, last_period_start_date, last_period_end_date = get_user_input()
    next_period_start = calculate_next_period(last_period_start_date, cycle_days)
    print(f"Your next period is expected to start on: {next_period_start}")
    
    current_date = datetime.now().date()
    current_phase = get_current_phase(last_period_start_date, current_date, cycle_days)
    print(f"Today's date: {current_date}")
    print(f"Current phase: {current_phase}")
    
    phase_info = get_phase_info(current_phase)
    if phase_info:
        print(f"Symptoms: {', '.join(phase_info['symptoms'])}")
        print(f"Recommended food: {', '.join(phase_info['food'])}")
        print(f"Exercises: {', '.join(phase_info['exercise'])}")
        print(f"Breathing techniques: {', '.join(phase_info['breathing'])}")
    else:
        print("Invalid phase or no information available.")
        
if __name__ == "__main__":
    main()