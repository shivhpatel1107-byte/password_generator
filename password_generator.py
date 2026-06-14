# Password Generator
# Generate strong, secure passwords automatically

import random
import string

def generate_password(length=12):
    """Generate a strong password with given length."""
    
    # Define character sets
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # !@#$%^&*() etc.
    
    # Create password character set (all characters)
    all_characters = lowercase + uppercase + digits + symbols
    
    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(all_characters)
    
    return password

def generate_strong_password(length=12):
    """Generate a strong password with guaranteed character types."""
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill remaining characters
    all_characters = lowercase + uppercase + digits + symbols
    remaining_length = length - 4
    
    for i in range(remaining_length):
        password.append(random.choice(all_characters))
    
    # Shuffle the password
    random.shuffle(password)
    
    return "".join(password)

def check_password_strength(password):
    """Check and display password strength."""
    
    strength_score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        strength_score += 1
        feedback.append("✅ Good length (8+ characters)")
    else:
        feedback.append("❌ Too short (should be 8+ characters)")
    
    if len(password) >= 12:
        strength_score += 1
        feedback.append("✅ Excellent length (12+ characters)")
    
    # Check for lowercase
    if any(char in string.ascii_lowercase for char in password):
        strength_score += 1
        feedback.append("✅ Contains lowercase letters")
    
    # Check for uppercase
    if any(char in string.ascii_uppercase for char in password):
        strength_score += 1
        feedback.append("✅ Contains uppercase letters")
    
    # Check for digits
    if any(char in string.digits for char in password):
        strength_score += 1
        feedback.append("✅ Contains numbers")
    
    # Check for symbols
    if any(char in string.punctuation for char in password):
        strength_score += 1
        feedback.append("✅ Contains symbols")
    
    # Determine strength level
    if strength_score >= 6:
        strength_level = "🔒 VERY STRONG"
    elif strength_score >= 4:
        strength_level = "🔐 STRONG"
    elif strength_score >= 3:
        strength_level = "⚠️ MODERATE"
    else:
        strength_level = "❌ WEAK"
    
    return strength_level, feedback

def display_password_info(password):
    """Display detailed password information."""
    
    print("\n" + "=" * 60)
    print("📊 PASSWORD ANALYSIS")
    print("=" * 60)
    print(f"🔑 Generated Password: {password}")
    print(f"📏 Length: {len(password)} characters")
    print("=" * 60)
    
    # Check strength
    strength_level, feedback = check_password_strength(password)
    
    print(f"\n💪 Strength Level: {strength_level}")
    print("\n📋 Feedback:")
    for item in feedback:
        print(f"  {item}")
    print("=" * 60)

def main():
    """Main program loop."""
    
    print("\n" + "=" * 60)
    print("🔐 PASSWORD GENERATOR - Generate Strong, Secure Passwords")
    print("=" * 60)
    
    while True:
        print("\nOptions:")
        print("1. Generate simple password")
        print("2. Generate strong password (recommended)")
        print("3. Check password strength")
        print("4. Quit")
        print("=" * 60)
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Get password length
            print("\n" + "=" * 60)
            try:
                length = int(input("Enter password length (default 12): ").strip())
                if length < 1:
                    print("❌ Length must be at least 1!")
                    continue
            except ValueError:
                length = 12  # Default
                print(f"Using default length: {length}")
            
            password = generate_password(length)
            display_password_info(password)
            
        elif choice == "2":
            # Get password length for strong password
            print("\n" + "=" * 60)
            try:
                length = int(input("Enter password length (default 12): ").strip())
                if length < 4:
                    print("❌ Length must be at least 4 for strong password!")
                    continue
            except ValueError:
                length = 12  # Default
                print(f"Using default length: {length}")
            
            password = generate_strong_password(length)
            display_password_info(password)
            
        elif choice == "3":
            # Check custom password strength
            print("\n" + "=" * 60)
            custom_password = input("Enter a password to check: ").strip()
            
            if custom_password:
                display_password_info(custom_password)
            else:
                print("❌ Password cannot be empty!")
            print("=" * 60)
            
        elif choice == "4":
            print("\n" + "=" * 60)
            print("👋 Thanks for using Password Generator! Stay Secure!")
            print("=" * 60)
            break
        
        else:
            print("\n❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        
        # Ask if user wants to generate another password
        if choice in ["1", "2"]:
            print("\n" + "=" * 60)
            another = input("\nGenerate another password? (yes/no): ").strip().lower()
            if another != "yes" and another != "y":
                print("\n" + "=" * 60)
                print("👋 Thanks for using Password Generator! Stay Secure!")
                print("=" * 60)
                break
            print("=" * 60)

if __name__ == "__main__":
    main()