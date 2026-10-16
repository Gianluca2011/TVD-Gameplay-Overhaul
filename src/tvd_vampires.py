
"""
TVD Gameplay Overhaul
Core vampire state and supernatural types.

This module defines the initial gameplay rules.
Game integration will be added in a later step.
"""

VAMPIRE = "vampire"
ORIGINAL = "original"
HYBRID = "hybrid"
HUMAN = "human"
WITCH = "witch"
SIPHONER = "siphoner"
HUNTER = "hunter"

VALID_TYPES = {
    VAMPIRE,
    ORIGINAL,
    HYBRID,
    HUMAN,
    WITCH,
    SIPHONER,
    HUNTER,
}


class VampireState:
    """Stores the TVD supernatural state for one Sim."""

    def __init__(self, supernatural_type=HUMAN):
        if supernatural_type not in VALID_TYPES:
            raise ValueError(
                "Unknown supernatural type: {}".format(
                    supernatural_type
                )
            )

        self.supernatural_type = supernatural_type
        self.blood_thirst = 0
        self.humanity_enabled = True
        self.is_ripper = False
        self.has_daylight_ring = False

    def become_vampire(self):
        if self.supernatural_type == HUMAN:
            self.supernatural_type = VAMPIRE
            self.blood_thirst = 0
            return True
        return False

    def become_original(self):
        if self.supernatural_type in (VAMPIRE, ORIGINAL):
            self.supernatural_type = ORIGINAL
            return True
        return False

    def become_hybrid(self):
        if self.supernatural_type in (VAMPIRE, HYBRID):
            self.supernatural_type = HYBRID
            return True
        return False

    def feed(self, amount=25):
        if self.supernatural_type not in (
            VAMPIRE, ORIGINAL, HYBRID
        ):
            return False

        amount = max(0, min(100, amount))
        self.blood_thirst = max(
            0, self.blood_thirst - amount
        )
        return True

    def increase_thirst(self, amount=5):
        if self.supernatural_type not in (
            VAMPIRE, ORIGINAL, HYBRID
        ):
            return False

        amount = max(0, amount)
        self.blood_thirst = min(
            100, self.blood_thirst + amount
        )
        return True

    def toggle_humanity(self):
        self.humanity_enabled = not self.humanity_enabled
        return self.humanity_enabled

    def toggle_ripper(self):
        if self.supernatural_type not in (
            VAMPIRE, ORIGINAL, HYBRID
        ):
            return False

        self.is_ripper = not self.is_ripper
        return self.is_ripper
