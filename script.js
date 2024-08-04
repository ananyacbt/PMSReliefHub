document.getElementById('cycle-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get user input values
    const periodDays = parseInt(document.getElementById('period-days').value, 10);
    const cycleDays = parseInt(document.getElementById('cycle-days').value, 10);
    const lastPeriodStartDate = document.getElementById('last-period-start').value;
    const lastPeriodEndDate = document.getElementById('last-period-end').value;

    // Validate inputs
    if (isNaN(periodDays) || isNaN(cycleDays) || !lastPeriodStartDate || !lastPeriodEndDate) {
        alert("Please ensure all fields are filled out correctly.");
        return;
    }

    if (periodDays < 1 || periodDays > 7 || cycleDays < 25 || cycleDays > 30) {
        alert("Please ensure period days are between 1-7 and cycle days are between 25-30.");
        return;
    }

    const nextPeriodStart = calculateNextPeriod(lastPeriodStartDate, cycleDays);
    const currentDate = new Date().toISOString().split('T')[0];
    const currentPhase = getCurrentPhase(lastPeriodStartDate, currentDate, cycleDays);
    const phaseInfo = getPhaseInfo(currentPhase);

    // Update the results
    document.getElementById('next-period').textContent = `Your next period is expected to start on: ${nextPeriodStart}`;
    document.getElementById('current-phase').textContent = `Today's date: ${currentDate}\nCurrent phase: ${currentPhase}`;

    document.getElementById('phase-symptoms').textContent = `Symptoms: ${phaseInfo.symptoms.join(', ')}`;
    document.getElementById('phase-food').textContent = `Recommended food: ${phaseInfo.food.join(', ')}`;
    document.getElementById('phase-exercise').textContent = `Exercises: ${phaseInfo.exercise.join(', ')}`;
    document.getElementById('phase-breathing').textContent = `Breathing techniques: ${phaseInfo.breathing.join(', ')}`;

    document.getElementById('result').classList.remove('hidden');
});

function calculateNextPeriod(lastPeriodStartDate, cycleDays) {
    const lastPeriodStart = new Date(lastPeriodStartDate);
    const nextPeriodStart = new Date(lastPeriodStart.getTime() + (cycleDays * 24 * 60 * 60 * 1000));
    return nextPeriodStart.toISOString().split('T')[0];
}

function getCurrentPhase(lastPeriodStartDate, currentDate, cycleDays) {
    const lastPeriodStart = new Date(lastPeriodStartDate);
    const current = new Date(currentDate);
    const cycleDay = Math.floor((current - lastPeriodStart) / (1000 * 60 * 60 * 24)) % cycleDays + 1;
    return trackMenstruationPhase(cycleDay);
}

function trackMenstruationPhase(cycleDay) {
    if (1 <= cycleDay && cycleDay <= 5) {
        return "Menstrual phase";
    } else if (6 <= cycleDay && cycleDay <= 14) {
        return "Follicular phase";
    } else if (15 <= cycleDay && cycleDay <= 16) {
        return "Ovulation phase";
    } else if (17 <= cycleDay && cycleDay <= 28) {
        return "Luteal phase";
    } else {
        return "Invalid day";
    }
}

function getPhaseInfo(phase) {
    const phaseInfo = {
        "Menstrual phase": {
            "symptoms": ["Cramps", "Fatigue", "Headaches", "Lower back pain", "Mood swings"],
            "food": ["Iron-rich foods", "Hydrating foods", "Leafy greens", "Lean meats", "Vitamin C-rich foods"],
            "exercise": ["Gentle yoga", "Walking", "Stretching", "Restorative yoga", "Light pilates"],
            "breathing": ["Deep breathing exercises", "Meditation", "Diaphragmatic breathing", "Body scan meditation"]
        },
        "Follicular phase": {
            "symptoms": ["Increased energy", "Improved mood", "Heightened creativity", "Enhanced cognitive function"],
            "food": ["Protein-rich foods", "Healthy fats", "Fresh fruits and vegetables", "Whole grains", "Nuts and seeds"],
            "exercise": ["Cardio", "Strength training", "High-intensity interval training (HIIT)", "Group fitness classes", "Cycling"],
            "breathing": ["Breath of fire", "Alternate nostril breathing", "Ujjayi breath", "Kapalbhati breathing"]
        },
        "Ovulation phase": {
            "symptoms": ["High energy", "Heightened senses", "Increased libido", "Ovulation pain (mittelschmerz)"],
            "food": ["Anti-inflammatory foods", "Antioxidants", "Berries", "Dark chocolate", "Omega-3 rich foods"],
            "exercise": ["High-intensity interval training (HIIT)", "Dancing", "Running", "Kickboxing", "Bootcamp classes"],
            "breathing": ["Cooling breath (Sheetali)", "Mindfulness breathing", "4-7-8 breathing", "Chandra Bhedana"]
        },
        "Luteal phase": {
            "symptoms": ["Bloating", "Mood swings", "Breast tenderness", "Fatigue", "Irritability", "Cravings"],
            "food": ["Complex carbs", "Magnesium-rich foods", "Bananas", "Dark leafy greens", "Seeds (pumpkin, sunflower)"],
            "exercise": ["Light cardio", "Stretching", "Yoga", "Swimming", "Low-impact aerobics"],
            "breathing": ["Box breathing", "Progressive relaxation", "Abdominal breathing", "Loving-kindness meditation"]
        }
    };
    return phaseInfo[phase] || {};
}


