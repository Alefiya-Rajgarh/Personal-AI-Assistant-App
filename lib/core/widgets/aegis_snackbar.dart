import 'package:flutter/material.dart';

import '../theme/aegis_colors.dart';

enum AegisSnackbarType { success, error, warning, info }

class AegisSnackbar {
  static void show(
    BuildContext context,
    String message,
    AegisSnackbarType type,
  ) {
    final color = _colorFor(type);
    final icon = _iconFor(type);

    final snackBar = SnackBar(
      behavior: SnackBarBehavior.floating,
      duration: const Duration(seconds: 3),
      backgroundColor: AssistantColors.surfaceDark,
      content: Row(
        children: [
          Container(
            width: 4,
            height: 32,
            decoration: BoxDecoration(
              color: color,
              borderRadius: BorderRadius.circular(4),
            ),
          ),
          const SizedBox(width: 12),
          Icon(icon, color: color),
          const SizedBox(width: 12),
          Expanded(
            child: Text(
              message,
              style: Theme.of(context)
                  .textTheme
                  .bodyMedium
                  ?.copyWith(color: AssistantColors.textPrimaryDark),
            ),
          ),
        ],
      ),
    );

    ScaffoldMessenger.of(context).showSnackBar(snackBar);
  }

  static Color _colorFor(AegisSnackbarType type) {
    switch (type) {
      case AegisSnackbarType.success:
        return AssistantColors.successDark;
      case AegisSnackbarType.error:
        return AssistantColors.errorDark;
      case AegisSnackbarType.warning:
        return AssistantColors.warningDark;
      case AegisSnackbarType.info:
        return AssistantColors.accentDark;
    }
  }

  static IconData _iconFor(AegisSnackbarType type) {
    switch (type) {
      case AegisSnackbarType.success:
        return Icons.check_circle_rounded;
      case AegisSnackbarType.error:
        return Icons.error_rounded;
      case AegisSnackbarType.warning:
        return Icons.warning_rounded;
      case AegisSnackbarType.info:
        return Icons.info_rounded;
    }
  }
}
