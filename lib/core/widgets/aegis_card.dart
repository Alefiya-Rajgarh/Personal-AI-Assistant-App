import 'package:flutter/material.dart';

import '../theme/aegis_colors.dart';
import '../theme/aegis_spacing.dart';

class AegisCard extends StatefulWidget {
  const AegisCard({
    super.key,
    required this.child,
    this.onTap,
  });

  final Widget child;
  final VoidCallback? onTap;

  @override
  State<AegisCard> createState() => _AegisCardState();
}

class _AegisCardState extends State<AegisCard> {
  bool _isPressed = false;

  @override
  Widget build(BuildContext context) {
    final card = Container(
      padding: const EdgeInsets.all(AssistanceSpacing.md),
      decoration: BoxDecoration(
        color: AssistantColors.surfaceDark,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: AssistantColors.cardBorderDark.withValues(alpha: 0.6),
        ),
      ),
      child: widget.child,
    );

    if (widget.onTap == null) {
      return card;
    }

    return AnimatedScale(
      scale: _isPressed ? 0.98 : 1,
      duration: const Duration(milliseconds: 120),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: widget.onTap,
          onTapDown: (_) => setState(() => _isPressed = true),
          onTapCancel: () => setState(() => _isPressed = false),
          onTapUp: (_) => setState(() => _isPressed = false),
          borderRadius: BorderRadius.circular(16),
          child: card,
        ),
      ),
    );
  }
}
