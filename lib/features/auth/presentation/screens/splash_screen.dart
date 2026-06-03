import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../../../core/theme/aegis_spacing.dart';
import '../../../../core/widgets/aegis_shimmer.dart';
import '../../../../core/widgets/aegis_button.dart';

class SplashScreen extends StatelessWidget {
  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(AssistanceSpacing.lg),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const AegisShimmer(width: 140, height: 140, borderRadius: 32),
              const SizedBox(height: AssistanceSpacing.lg),
              Text(
                'Assistant AI',
                style: Theme.of(context).textTheme.displayMedium,
              ),
              const SizedBox(height: AssistanceSpacing.sm),
              Text(
                'Preparing your executive workspace...',
                style: Theme.of(context).textTheme.bodyMedium,
              ),
              const SizedBox(height: AssistanceSpacing.xl),
              AegisButton(
                label: 'Continue',
                onPressed: () => context.go('/onboarding'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
