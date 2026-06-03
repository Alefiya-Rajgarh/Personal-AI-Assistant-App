import 'package:flutter/material.dart';

import '../theme/aegis_colors.dart';

enum AegisChipVariant { filled, outlined, subtle }

class AegisChip extends StatelessWidget {
  const AegisChip({
    super.key,
    required this.label,
    this.variant = AegisChipVariant.filled,
  });

  final String label;
  final AegisChipVariant variant;

  @override
  Widget build(BuildContext context) {
    final style = Theme.of(context).textTheme.labelSmall;
    Color background;
    Color foreground;
    BoxBorder? border;

    switch (variant) {
      case AegisChipVariant.outlined:
        background = Colors.transparent;
        foreground = AssistantColors.primaryDark;
        border = Border.all(color: AssistantColors.primaryDark);
        break;
      case AegisChipVariant.subtle:
        background = AssistantColors.primaryDark.withValues(alpha: 0.1);
        foreground = AssistantColors.primaryDark;
        border = null;
        break;
      case AegisChipVariant.filled:
        background = AssistantColors.primaryDark;
        foreground = Colors.white;
        border = null;
        break;
    }

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      decoration: BoxDecoration(
        color: background,
        borderRadius: BorderRadius.circular(20),
        border: border,
      ),
      child: Text(
        label,
        style: style?.copyWith(color: foreground),
      ),
    );
  }
}
