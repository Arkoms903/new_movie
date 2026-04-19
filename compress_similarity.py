import pickle
import gzip
import os

print("=" * 50)
print("SIMILARITY FILE COMPRESSION SCRIPT")
print("=" * 50)

# Check if original file exists
if not os.path.exists("similarity.pkl"):
    print("❌ ERROR: similarity.pkl not found!")
    print("Make sure you're in the correct directory")
    exit(1)

# Get original file size
original_size = os.path.getsize("similarity.pkl")
print(f"\n📊 Original file size: {original_size / (1024**2):.2f} MB")

# Load the file
print("\n⏳ Loading similarity.pkl...")
try:
    similarity = pickle.load(open("similarity.pkl", "rb"))
    print("✅ Successfully loaded!")
except Exception as e:
    print(f"❌ Error loading file: {e}")
    exit(1)

# Compress the file
print("\n⏳ Compressing file...")
try:
    with gzip.open("similarity.pkl.gz", "wb") as f:
        pickle.dump(similarity, f)
    print("✅ Successfully compressed!")
except Exception as e:
    print(f"❌ Error compressing: {e}")
    exit(1)

# Get compressed file size
compressed_size = os.path.getsize("similarity.pkl.gz")
print(f"\n📊 Compressed file size: {compressed_size / (1024**2):.2f} MB")

# Calculate compression ratio
ratio = (1 - compressed_size / original_size) * 100
print(f"📈 Compression ratio: {ratio:.1f}%")

# Verify the compressed file
print("\n⏳ Verifying compressed file...")
try:
    test_data = pickle.load(gzip.open("similarity.pkl.gz", "rb"))
    print(f"✅ Verification successful!")
    print(f"   Shape: {test_data.shape}")
except Exception as e:
    print(f"❌ Verification failed: {e}")
    exit(1)

print("\n" + "=" * 50)
print("🎉 COMPRESSION COMPLETE!")
print("=" * 50)
print("\n✅ You can now delete similarity.pkl (optional)")
print("✅ Upload similarity.pkl.gz to GitHub")
print("\nNext steps:")
print("1. Add similarity.pkl to .gitignore")
print("2. Push similarity.pkl.gz to GitHub")
print("3. Deploy to Render")