import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';

import '../theme/aegis_colors.dart';

class AegisAvatar extends StatelessWidget {
  const AegisAvatar({
    super.key,
    this.imageUrl,
    this.initials = 'AI',
    this.size = 48,
    this.isOnline = false,
  });

  final String? imageUrl;
  final String initials;
  final double size;
  final bool isOnline;

  @override
  Widget build(BuildContext context) {
    final avatar = ClipOval(
      child: SizedBox(
        width: size,
        height: size,
        child: imageUrl == null
            ? Container(
                color: AssistantColors.primaryDark,
                alignment: Alignment.center,
                child: Text(
                  initials,
                  style: Theme.of(context)
                      .textTheme
                      .titleMedium
                      ?.copyWith(color: Colors.white),
                ),
              )
            : CachedNetworkImage(
                imageUrl: imageUrl!,
                fit: BoxFit.cover,
              ),
      ),
    );

    if (!isOnline) {
      return avatar;
    }

    return Stack(
      alignment: Alignment.bottomRight,
      children: [
        avatar,
        Container(
          width: size * 0.22,
          height: size * 0.22,
          decoration: BoxDecoration(
            color: AssistantColors.successDark,
            shape: BoxShape.circle,
            border: Border.all(color: AssistantColors.backgroundDark, width: 2),
          ),
        ),
      ],
    );
  }
}
