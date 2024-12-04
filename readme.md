## Fixed Issues

### Password Security (Issue #3)
**Status**: Closed

I added stronger password rules and better security:
- Made passwords require at least 8 characters
- Must have uppercase, lowercase, numbers, and special characters
- Added proper password hashing with bcrypt
- Set up account lockouts after failed login attempts

The changes make it much harder for attackers to guess or crack passwords, while still keeping things user-friendly.

### Nickname Rules (Issue #2)
**Status**: Closed

I fixed nickname validation to prevent issues:
- Must be 3-30 characters long
- Only letters, numbers, underscores, and hyphens allowed
- Can't use reserved words like 'admin' or 'system'
- Added clear error messages when validation fails

This makes nicknames both safer and easier to use.

### Registration Error Fix (Issue #1)
**Status**: Closed

Fixed the 500 error that happened when someone tried to register with an email that was already used. Now it shows a clear message instead of crashing.

## What I Learned
This project taught me a lot about security and user experience. The biggest lessons were:

1. Good password security needs both strong rules and good user feedback
2. Testing different scenarios early catches problems before they hit production
3. Clear error messages make a huge difference in user experience

## Testing
I added lots of tests to make sure everything works:
- Tested all the new password rules
- Checked nickname validation edge cases
- Made sure error messages show up correctly
- Current test coverage is at 92%
