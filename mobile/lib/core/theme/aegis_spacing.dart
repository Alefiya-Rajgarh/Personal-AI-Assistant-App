import 'package:flutter/material.dart';

class AssistanceSpacing {
  static const double xs = 4;
  static const double sm = 8;
  static const double md = 16;
  static const double lg = 24;
  static const double xl = 32;
  static const double xxl = 48;
}

class AssistanceRadius {
  static const double sm = 8.0;
  static const double md = 12.0;
  static const double lg = 16.0;
  static const double xl = 24.0;
  static const double full = 999.0;
}

class AssistanceShadows {
  static final BoxShadow subtle = BoxShadow(
    color: Colors.black.withValues(alpha: 0.08),
    blurRadius: 3,
    offset: const Offset(0, 1),
  );

  static final BoxShadow medium = BoxShadow(
    color: Colors.black.withValues(alpha: 0.12),
    blurRadius: 16,
    offset: const Offset(0, 4),
  );

  static final BoxShadow strong = BoxShadow(
    color: Colors.black.withValues(alpha: 0.2),
    blurRadius: 32,
    offset: const Offset(0, 8),
  );
}
