import 'package:flutter/material.dart';

import '../theme/aegis_colors.dart';
import '../theme/aegis_spacing.dart';
import 'aegis_button.dart';

class AegisEmptyState extends StatelessWidget {
  const AegisEmptyState({
    super.key,
    required this.icon,
    required this.title,
    required this.subtitle,
    this.ctaLabel,
    this.onCtaPressed,
  });

  final IconData icon;
  final String title;
  final String subtitle;
  final String? ctaLabel;
  final VoidCallback? onCtaPressed;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(AssistanceSpacing.lg),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              icon,
              size: 64,
              color: AssistantColors.primaryDark.withValues(alpha: 0.2),
            ),
            const SizedBox(height: AssistanceSpacing.md),
            Text(title, style: Theme.of(context).textTheme.headlineSmall),
            const SizedBox(height: AssistanceSpacing.sm),
            Text(
              subtitle,
              style: Theme.of(context)
                  .textTheme
                  .bodyMedium
                  ?.copyWith(color: AssistantColors.textSecondaryDark),
              textAlign: TextAlign.center,
            ),
            if (ctaLabel != null && onCtaPressed != null) ...[
              const SizedBox(height: AssistanceSpacing.lg),
              AegisButton(label: ctaLabel!, onPressed: onCtaPressed),
            ],
          ],
        ),
      ),
    );
  }
}
