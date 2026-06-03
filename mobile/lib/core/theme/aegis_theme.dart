import 'package:flutter/material.dart';

import 'aegis_colors.dart';
import 'aegis_text_styles.dart';

class AegisTheme {
  static final ThemeData darkTheme = ThemeData(
    useMaterial3: true,
    scaffoldBackgroundColor: AssistantColors.backgroundDark,
    cardColor: AssistantColors.surfaceDark,
    colorScheme: const ColorScheme.dark(
      primary: AssistantColors.primaryDark,
      secondary: AssistantColors.secondaryDark,
      surface: AssistantColors.surfaceDark,
      onSurface: AssistantColors.textPrimaryDark,
      error: AssistantColors.errorDark,
    ),
    appBarTheme: const AppBarTheme(
      backgroundColor: Colors.transparent,
      elevation: 0,
      centerTitle: true,
      iconTheme: IconThemeData(color: Colors.white),
    ),
    textTheme: _buildTextTheme(AssistantColors.textPrimaryDark),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        foregroundColor: AssistantColors.primaryDark,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AssistantColors.primaryDark,
        foregroundColor: Colors.white,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        foregroundColor: AssistantColors.primaryDark,
        side: const BorderSide(color: AssistantColors.primaryDark),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: AssistantColors.surfaceDark,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(
          color: AssistantColors.primaryDark,
          width: 1.5,
        ),
      ),
      errorBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(
          color: AssistantColors.errorDark,
          width: 1.5,
        ),
      ),
    ),
    cardTheme: CardThemeData(
      color: AssistantColors.surfaceDark,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    ),
  );

  static final ThemeData lightTheme = ThemeData(
    useMaterial3: true,
    scaffoldBackgroundColor: AssistantColors.backgroundLight,
    cardColor: AssistantColors.surfaceLight,
    colorScheme: const ColorScheme.light(
      primary: AssistantColors.primaryLight,
      secondary: AssistantColors.secondaryLight,
      surface: AssistantColors.surfaceLight,
      onSurface: AssistantColors.textPrimaryLight,
      error: AssistantColors.errorLight,
    ),
    appBarTheme: const AppBarTheme(
      backgroundColor: Colors.transparent,
      elevation: 0,
      centerTitle: true,
      iconTheme: IconThemeData(color: AssistantColors.textPrimaryLight),
    ),
    textTheme: _buildTextTheme(AssistantColors.textPrimaryLight),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        foregroundColor: AssistantColors.primaryLight,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AssistantColors.primaryLight,
        foregroundColor: Colors.white,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        foregroundColor: AssistantColors.primaryLight,
        side: const BorderSide(color: AssistantColors.primaryLight),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: AssistantColors.surface2Light,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(
          color: AssistantColors.primaryLight,
          width: 1.5,
        ),
      ),
      errorBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(
          color: AssistantColors.errorLight,
          width: 1.5,
        ),
      ),
    ),
    cardTheme: CardThemeData(
      color: AssistantColors.surfaceLight,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    ),
  );

  static TextTheme _buildTextTheme(Color textColor) {
    return TextTheme(
      displayLarge: AegisTextStyles.displayLarge.copyWith(color: textColor),
      displayMedium: AegisTextStyles.displayMedium.copyWith(color: textColor),
      headlineLarge: AegisTextStyles.headingLarge.copyWith(color: textColor),
      headlineMedium: AegisTextStyles.headingMedium.copyWith(color: textColor),
      headlineSmall: AegisTextStyles.headingSmall.copyWith(color: textColor),
      titleLarge: AegisTextStyles.titleLarge.copyWith(color: textColor),
      titleMedium: AegisTextStyles.titleMedium.copyWith(color: textColor),
      bodyLarge: AegisTextStyles.bodyLarge.copyWith(color: textColor),
      bodyMedium: AegisTextStyles.bodyMedium.copyWith(color: textColor),
      bodySmall: AegisTextStyles.bodySmall.copyWith(color: textColor),
      labelLarge: AegisTextStyles.labelLarge.copyWith(color: textColor),
      labelSmall: AegisTextStyles.labelSmall.copyWith(color: textColor),
    );
  }
}
