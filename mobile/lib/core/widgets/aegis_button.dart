import 'package:flutter/material.dart';

import '../theme/aegis_colors.dart';

enum AegisButtonVariant { primary, secondary, ghost, danger }

class AegisButton extends StatefulWidget {
  const AegisButton({
    super.key,
    required this.label,
    this.onPressed,
    this.variant = AegisButtonVariant.primary,
    this.isLoading = false,
    this.fullWidth = true,
  });

  final String label;
  final VoidCallback? onPressed;
  final AegisButtonVariant variant;
  final bool isLoading;
  final bool fullWidth;

  @override
  State<AegisButton> createState() => _AegisButtonState();
}

class _AegisButtonState extends State<AegisButton> {
  bool _isPressed = false;

  @override
  Widget build(BuildContext context) {
    final colors = _variantColors(widget.variant, Theme.of(context));

    final content = widget.isLoading
        ? const SizedBox(
            width: 20,
            height: 20,
            child: CircularProgressIndicator(
              strokeWidth: 2,
              valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
            ),
          )
        : Text(
            widget.label,
            style: Theme.of(context)
                .textTheme
                .labelLarge
                ?.copyWith(color: colors.foreground),
          );

    return AnimatedScale(
      scale: _isPressed ? 0.97 : 1,
      duration: const Duration(milliseconds: 120),
      child: SizedBox(
        width: widget.fullWidth ? double.infinity : null,
        height: 48,
        child: Material(
          color: colors.background,
          borderRadius: BorderRadius.circular(12),
          child: InkWell(
            onTap: widget.isLoading ? null : widget.onPressed,
            onTapDown: (_) => setState(() => _isPressed = true),
            onTapCancel: () => setState(() => _isPressed = false),
            onTapUp: (_) => setState(() => _isPressed = false),
            borderRadius: BorderRadius.circular(12),
            child: Center(child: content),
          ),
        ),
      ),
    );
  }
}

class _AegisButtonColors {
  const _AegisButtonColors({required this.background, required this.foreground});

  final Color background;
  final Color foreground;
}

_AegisButtonColors _variantColors(
  AegisButtonVariant variant,
  ThemeData theme,
) {
  switch (variant) {
    case AegisButtonVariant.secondary:
      return const _AegisButtonColors(
        background: AssistantColors.secondaryDark,
        foreground: Colors.white,
      );
    case AegisButtonVariant.ghost:
      return _AegisButtonColors(
        background: Colors.transparent,
        foreground: theme.colorScheme.primary,
      );
    case AegisButtonVariant.danger:
      return const _AegisButtonColors(
        background: AssistantColors.errorDark,
        foreground: Colors.white,
      );
    case AegisButtonVariant.primary:
      return const _AegisButtonColors(
        background: AssistantColors.primaryDark,
        foreground: Colors.white,
      );
  }
}
